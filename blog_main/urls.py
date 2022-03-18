"""blog_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 위에서 부터 순서 대로 매칭 되는지 확인
urlpatterns = [
    path('blog/', include('blog.urls')), # 블로그 디렉토리 안의 urls.py에 있는 url패턴으로 넘긴다. 2차 라우팅
    path('admin/', admin.site.urls), # 대충 admin/로 시작하면 admin.site.urls로 보낸다는 뜻 (패턴, 수행할 작업)
    # 수행할 작업에 함수를 넣어 주는 것 -> FBV
    # 수행할 작업에 이미 만들어 놓은 뷰(클래스)를 넣어 주는 경우도 있다.
] # 여기 우리가 처리할 패턴들을 적으면 된다.
