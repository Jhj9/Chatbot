import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .apps import MainConfig
import torch


def index(request):
    return render(request, 'main/index.html')


def demo(request):
    return render(request, f'main/demo.html')



@csrf_exempt
def submit(request):
        
    # apps.py에서 정의된 변수 사용 가능
    # ex) MainConfig.model
        
    response = {"answer_response": "출렁다리란 보행자 전용교량의 한 종류로서 케이블에 의해 지어지며, 보행 시 흔들림을 허용하는 유연 보행교입니다.",
        "answer_source": "03출렁다리 유지관리 매뉴얼 해설서",
        "answer_page": 17,
        "answer_document": "제2장 출렁다리 일반 13 제2장 출렁다리 일반 21 출렁다리의 정의 출렁다리란 보행자 전용교량의 한 종류로서 케이블에 의해 지되며 보행시 흔들림을 허용하는 유연 보행교로 정의한다 해설 케이블에 의해 지되는 보도교로는 현수교와 사장교 아치교 형태 등이 있다 대상 구조 물에 대한 분류 과정에서 현수교와 사장교 아치교 형태 등 모든 케이블 보도교를 출렁다 리에 포함시키는 방안에 대해 검토하였으나 사장교 및 아치교 형태의 보도교는 보강거더 의 강성이 커서 흔들림이 크지 않고 지금까지 국내에 시공된 출렁다리 중 현수교 이외의 형태는 5 이하로 조사되어 출렁다리 대상구조물에서 제외하였다 현수교 형태의 보도교 경우에도 보강거더의 강성을 크게 설계하는 경우에는 흔들림의 크지 않으나 현수교 타입 은 어느 정도의 흔들림이 발생되는 점을 고려하여 보강거더의 강성이 큰 현수교 형태의 보 도교도 출렁다리에 포함하였다 2 출렁다리의 구성 21 부재별 명칭 출렁다리를 구성하는 주요 요소는 크게 다음과 같이 구분할 수 있다 1 보강거더 보행자를 지하는 부재 2 행어 보강거더를 매다는 연결재 3 주 케이블 행어를 매다는 현수재 4 바닥 케이블 보강거더를 고정시키는 케이블 5 내풍 케이블Wind Cable 보강거더의 횡방향 진동을 제어하기 위한 케이블 6 주탑 주 케이블을 지하는 부재 7 보조주탑 강주탑과 기초사이에 설치되어 주탑의 하중을 기초로 전달하는 콘크리트 기둥 8 기초 주탑 또는 보조주탑을 지하며 하중을 지반으로 전달하는 부재"
        }

    return JsonResponse(response)