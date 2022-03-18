from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # methods
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    # 나중에 url 패턴을 바꾸더라도 문제가 없다.
    # admin 페이지에 갑자기 붙어버린다.
    # 인터페이스를 오버라이딩
    # 장고같은 프레임워크(convention of configuration): 이름을 어떻게 정하느냐에 따라 알아서 작동하는 인터페이스가 많이 정의되어있다.