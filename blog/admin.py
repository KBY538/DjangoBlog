from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) # admin 사이트에 Post 등록하면 접근 가능한 인터페이스 자동 생성