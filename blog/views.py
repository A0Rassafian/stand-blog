from django.shortcuts import render ,get_object_or_404

from blog.models import Article, Category
from django.core.paginator import Paginator

# Create your views here.





def article_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return render(request,"blog/article_detail.html",{"article":article})



def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles,2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request,"blog/article_list.html" , {"articles":articles})


def category_detail(request,pk):
    category = get_object_or_404(Category,id=pk)
    articles = category.articles.all()
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request,"blog/article_list.html",{"articles":articles})