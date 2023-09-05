# 문맥에 맞는 대화 응답 자동 생성 및 응답 적절성 평가 프로그램
문맥에 맞는 대화 응답 자동 생성 및 응답 적절성 평가 프로그램

프로그램 소개
대화 응답 자동 평가 관련 연구를 진행하면서, 문맥에 맞는 대화의 응답을 자동으로 생성하고 평가하는 과정을 사용자들이 쉽게 체험해 볼 수 있도록 개발된 프로그램이다. 자동으로 생성된 응답이 대화 내에서 얼마나 적절한지 평가하여, 생성된 응답에 대한 단어 및 문맥 레벨의 스코어를 확인할 수 있다. 무료 오픈소스 웹 어플리케이션 프레임워크인 Django를 이용해 제작되었으며, 프로그램의 개발을 위해 HTML, CSS, JavaScript, Python 등의 언어가 사용되었다. <br>

주요 기능
- 프로그램에 적용된 대화 응답 자동 평가 연구가 진행된 배경 및 연구를 진행하는 목적 등, 프로그램의 전반적인 설명을 제공한다. <br>
- 예제 대화의 문맥에 맞는 응답을 자동으로 생성하여 생성된 결과를 평가 스코어와 함께 출력한다. <br>
- 생성된 응답에 대한 단어 레벨 및 문맥 레벨의 스코어를 계산하고, 사용자들이 결과를 파악하기 쉽도록 시각적 효과를 적용하여 나타낸다. <br>
- 사용자들이 여러 예제에 대해서 체험해볼 수 있도록 다양한 대화 예제를 제공한다. <br>

사용 방법
1. 왼쪽 상단의 탭에서 Description 페이지와 Demo 페이지로 이동할 수 있다. <br>
2. Description - 연구의 진행 배경 및 목적에 대한 정보를 얻을 수 있다. <br>
3. Demo - 실제 예제를 테스트 해볼 수 있다. <br>
3-1. Generate 버튼을 누르면 대화의 문맥에 맞는 응답이 자동 생성되며, 단어 및 문맥 레벨의 평가 스코어를 확인할 수 있다. <br>
3-2. Generate 버튼을 다시 누르면 동일한 대화에 대한 새로운 응답이 자동 생성되며, 스코어를 확인할 수 있다. <br>
3-3. Next 버튼을 누르면 새로운 대화 예제에 대해서 테스트 해볼 수 있다. <br>

Pycharm

![화면 캡처 2022-04-13 141152](https://user-images.githubusercontent.com/50137851/163105666-d975d5a9-6f46-4015-bd12-92cf726cc163.png)

1) Get from VCS로 시작하기

2) https://github.com/Jhj9/Conversation-Response-Generation-Demo.git clone<br>

3) pip install -r requirements.txt<br>

5) mysite/secrets.json 생성 후 SECRET_KEY 입력 <br>
  Ex) {"SECRET_KEY": "django-insecure-dml=장고시크릿키50자"} <br>
  https://djecrety.ir/

6) Terminal에 python manage.py runserver 입력<br>

7) http://127.0.0.1:8000/ 웹페이지 실행
