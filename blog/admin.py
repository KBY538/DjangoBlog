from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
admin.site.register(Post) # admin 사이트에 Post 등록하면 접근 가능한 인터페이스 자동 생성
# 사실 이렇게 한 줄로 쓰는 게 특이 케이스

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name', )} # 딕셔너리 이용해서 slug 타입 값에는 name을 그대로 넣으라는 뜻(뒤에다 튜플을 넣는다)
    # slug을 name으로부터 생성해서 채우도록

admin.site.register(Category, CategoryAdmin) # 쌍으로 묶어서 register

class TagAdmin(admin.ModelAdmin):
    propopulated_fields = {'slug':('name', )}

admin.site.register(Tag, TagAdmin)