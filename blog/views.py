from django.shortcuts import render # 템플릿을 클라이언트에 뿌려주는 흔히 쓰는 함수
from django.views.generic import ListView, DetailView

from .models import Post, Category, Tag


# 장고는 sql 쿼리를 직접 안 날려도 됨. 임포트만으로 db 연결. 다 메소드로 매핑되어있다.
# 복잡한 쿼리를 처리하고 싶다면 Post 안에 해당 쿼리를 처리하는 메소드를 만들면 됨

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html' # 템플릿 이름을 지정할 수 있다.
    # 다른 사람들과 작업할 때 강제할당하는 건 좋지 않고 name convention에 익숙해지는 게 좋다.

    # get_context_data 오버라이드
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data() # 이미 있는 애들 포함

        # 추가적으로 넘겨주고 싶은 context가 있을 때 많이 쓰는 패턴

        context['categories'] = Category.objects.all() # 모든 카테고리의 목록 싹다
        # 특정 필터의 object의 값들만 가져옴
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        # 카테고리가 None인 애들을 찾아서 목록을 가져온다. 필터로넣어줄 조건은 카테고리가 None일 것.
        #목록을 가져온 다음에 view단에서 len할 수도 있고 그냥 숫자만 넘겨주려고 count를 할 수도 있고

        return context # 이렇게 변경한 context를 넘겨줘야 context가 넘어간다. return 꼭 해줘야

# 명시적로 넘주지 않기 때문에 _list

class PostDetail(DetailView):
    model = Post
    # _detail이 자동으로, post라고 넘긴다

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

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


def show_category_posts(request, slug):

    # 하드코딩 방식
    if slug=='no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'category' : category,
        'post_list' : post_list
    }
    return render(request, 'blog/post_list.html', context)


def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    context = {
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'tag': tag,
        'post_list': tag.post_set.all()
    }
    return render(request, 'blog/post_list.html', context)