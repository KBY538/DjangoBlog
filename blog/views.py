from django.shortcuts import render # 템플릿을 클라이언트에 뿌려주는 흔히 쓰는 함수
from django.views.generic import ListView, DetailView

from .models import Post
# 장고는 sql 쿼리를 직접 안 날려도 됨. 임포트만으로 db 연결. 다 메소드로 매핑되어있다.
# 복잡한 쿼리를 처리하고 싶다면 Post 안에 해당 쿼리를 처리하는 메소드를 만들면 됨

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html' # 템플릿 이름을 지정할 수 있다.
    # 다른 사람들과 작업할 때 강제할당하는 건 좋지 않고 name convention에 익숙해지는 게 좋다.

# 명시적으로 넘겨주지 않기 때문에 _list

class PostDetail(DetailView):
    model = Post
    # _detail이 자동으로, post라고 넘긴다

# def index(request):
#
#     posts = Post.objects.all().order_by('-pk') # Post로부터 모든 object를 싹다 꺼내는 작업을 한다.
#
#     return render(
#         request,
#         'blog/index.html', # convention over configuration, 우리가 안 만들었는데 프레임워크가 알아서 정해놓은 거, blog 안의 templates 안의 blog 안의 index.html
#         {
#             'posts': posts, # posts라는 이름으로 방금 꺼낸 posts를 할당
#         } # context, 키에 해당되는 posts를 html 파일 안에서 변수로 취급해 접근 가능, 키 이름에 신경쓰기
#         # html이라고 되어있지만 장고 template language라는 별도의 언어로 되어있다.
#         # 우리가 db에서 찾아온 것을 context를 통해 실어 보내줌.
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # pk 필드의 값이 방금 매개변수로 넘겨받은 pk와 같은 레코드를 뽑아오고 싶다.

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )