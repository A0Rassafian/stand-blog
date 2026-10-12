from django.shortcuts import render
from blog.models import Article
from django.urls import reverse
# Create your views here.



def home(request):
    articles = Article.objects.all()
    # print(reverse("blog:article_detail",args=(1,)))
    resent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request,"home/index.html" ,{"articles":articles})