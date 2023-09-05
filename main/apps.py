from django.apps import AppConfig

import logging
import torch
from transformers import GenerationConfig, AutoModelForQuestionAnswering, AutoTokenizer, pipeline, AutoModelForCausalLM, AutoConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    # 서버 실행시킬 때 한번만 load해도 되는 것, load 시간이 오래 걸리는 것 정의 ex) model
    # ex) model = ~~~~~
    