from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(staus='published')

    options=(
        ('draft','Draft'),
        ('published','Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title=models.CharField(max_length=200)
    exceprt=models.CharField(null=True)
    content=models.TextField()
    slug=models.SlugField(max_length=200,unique_for_date='published')
    published=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    staus=models.CharField(max_length=10,choices=options,default='published')
    objects=models.Manager() #default manager
    postobjects=PostObjects() #custom manager
  

    class meta:
        ordering=('-published',)

    def __str__(self):
        return self.title