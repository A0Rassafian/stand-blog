from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(is_published=True)







class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Article(models.Model):
    # CHOICES =(
    # ("A","پایتون"),
    # ("B", "java"),
    # )
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='articles')
    category = models.ManyToManyField(Category , related_name='articles')
    title = models.CharField(max_length=70
                             , help_text="Title of the article",unique=True
                             # ,unique=True
                             # db_column='mytitle'
                             # null=True,
                             # blank=True,
                             # editable=False,
                             # choices=CHOICES,
                             # unique_for_date="published"

                             )
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    # published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)
    objects = models.Manager()
    custom_manager=ArticleManager()


    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={'slug':self.slug})



    def __str__(self):
        return self.title


    def save(self , *args,**kwargs):
        print(self.title)
        self.slug = slugify(self.title)
        super(Article ,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-created']
        verbose_name = "Article"
        verbose_name_plural = "Articles"


