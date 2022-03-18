from django.urls import path, include

from . import views # .을 찍는 게 blog라고 적는 것보다 에러가 덜 난다.

urlpatterns = [
    path('<int:pk>/', views.single_post_page), # 매개변수에 pk를 전달하는 건 지맘대로 이름이 일치하는 거 찾아서 해버림
    # <자료형:변수명> pk라는 이름으로 single_post_page에 전달이 될 것이다.
    path('', views.index), # 템플릿을 구현할 함수를 수행할 작업에 넣는다.
]
