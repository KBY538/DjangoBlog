from django.urls import path, include

from . import views # .을 찍는 게 blog라고 적는 것보다 에러가 덜 난다.

urlpatterns = [
    # path('12/', blah) # 이렇게 해두면 더 위에 있으니 먼저 처리
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    #path('<int:pk>/', views.single_post_page), # 매개변수에 pk를 전달하는 건 지맘대로 이름이 일치하는 거 찾아서 해버림
    # <자료형:변수명> pk라는 이름으로 single_post_page에 전달이 될 것이다.
    #path('', views.index), # 템플릿을 구현할 함수를 수행할 작업에 넣는다.
    path('category/<str:slug>/', views.show_category_posts) # 이미 만든 PistList를 활용하자. 해당되는 카테고리의 post만 list되도록
]
