import os.path

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) # 같은 이름을 가진 카테고리가 여러 개 생기면 안 되니까 unique
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook = models.TextField(blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)  # media파일 아래 어디에다가 피일을 저장할 것인가, 첨부하지 않아도 된다
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True) # 파일 하나만

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    # 기본 제공되는 user를 쓰면 로그인도 간단하게 처리된다.
    # on_delete 시, CASCADE함수를 실행. 콜백함수를 설정하는 것, CASCADE()하면 결과를 return해서 쓰는 게 된다. 커스텀 함수를 만들 수도있다. models에서
    # foreign key는 null이면 안 된다.
    # 첫 번째 옵션: default 값을 알아서 만들어준다.(admin
    # 두 번째 옵션: author 필드에다가 default를 넣어준다.
    # 첫 번째가 쉬운 길
    # 1번 선택하고 pk 넣어주면 된다.(1번 유저가 어드민)

    # 프론트엔드 단에서와 서버 단에서 검증을 두 번 한다
    # 모델에 들어가기 전에 값이 비어있어도 되는가 여기서의 null 키워드는 서버의 모델에 저장할 때
    # 프론트 엔드 쪽에서 공란일 수 있는지 체크는 따로 있다. 그게 blank

    # methods
    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_file_name(self):
        return os.path.basename(self.attached_file.name)

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    # 나중에 url 패턴을 바꾸더라도 문제가 없다.
    # admin 페이지에 갑자기 붙어버린다.
    # 인터페이스를 오버라이딩
    # 장고같은 프레임워크(convention of configuration): 이름을 어떻게 정하느냐에 따라 알아서 작동하는 인터페이스가 많이 정의되어있다.
