from django.apps import AppConfig

import os
import logging
import torch
from haystack.document_stores import InMemoryDocumentStore
from haystack.pipelines.standard_pipelines import TextIndexingPipeline
from transformers import GenerationConfig, AutoModelForQuestionAnswering, AutoTokenizer, pipeline, AutoModelForCausalLM
from haystack.nodes import BM25Retriever, EmbeddingRetriever
from haystack.utils import print_answers

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    summarize_before_qa = False
    bm25 = False

    # logger 설정
    logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
    logging.getLogger("haystack").setLevel(logging.INFO)


    #qa_model_name = "ainize/klue-bert-base-mrc"
    completion_model_name = 'beomi/KoAlpaca-Polyglot-12.8B'
    ###generation_config = GenerationConfig.from_pretrained(completion_model_name)
    
    
    # document_store에 문서 위치 지정하기

    doc_dir = os.getcwd()+"/data"
    files_to_index = [os.getcwd()+"/data" + '/' + f for f in os.listdir(doc_dir)]

    # Meta creation List[Dict[str, Any]]
    # We make a list of dicts containing the filenames of the docs as "name" field for indexing
    meta_file_list = [dict(name=file) for file in files_to_index]


    # We debug by checking whether the docs got their meta fields as we wanted (name of file)
    # document_store.get_document_by_id(candidate_documents[0].id).meta["name"]
    # document_store.get_all_documents()[0]

    # 모델 불러오기
    ''' 1: Retriever '''
    if bm25:
        document_store = InMemoryDocumentStore(use_bm25=True)
        indexing_pipeline = TextIndexingPipeline(document_store)
        indexing_pipeline.run_batch(file_paths=files_to_index, meta=meta_file_list)
        retriever = BM25Retriever(document_store=document_store)
    else:
        document_store = InMemoryDocumentStore(embedding_dim=1024)
        indexing_pipeline = TextIndexingPipeline(document_store)
        indexing_pipeline.run_batch(file_paths=files_to_index, meta=meta_file_list)
        retriever = EmbeddingRetriever(document_store=document_store, 
                                embedding_model='intfloat/multilingual-e5-large', 
                                model_format="sentence_transformers")
        document_store.update_embeddings(retriever)
    
    #torch.cuda.empty_cache()
    
    ''' 2: Reader '''
    # qa_model = AutoModelForQuestionAnswering.from_pretrained(qa_model_name)   
    # tokenizer = AutoTokenizer.from_pretrained(qa_model_name)

    completion_model = AutoModelForCausalLM.from_pretrained(
        completion_model_name,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to(device=device, non_blocking=True)
    
    completion_model.eval()

    pipe = pipeline(
        'text-generation', 
        model=completion_model,
        tokenizer=completion_model_name,
        device=device
    )
    
    #torch.cuda.empty_cache()