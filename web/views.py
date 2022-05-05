from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse('欢迎使用Django！')


from web.models import Category, Banner, Article
#把Banner表导入
def index(request):
    # 通过Category表查出所有分类
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]  # 查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    #把查询出来的分类封装到上下文里
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        }
    return render(request, 'index.html', context)