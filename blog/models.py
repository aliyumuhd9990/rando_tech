from django.db import models
from accounts.models import *
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog:post_list_by_category', args=[self.slug])

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')
class Post(models.Model):
    STATUS_CHOICES = {
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    }
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    cover_img = models.ImageField(upload_to='img/post_cover', blank=True, null=False, default='img/blog-1.jpg')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    
    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             null=True, blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    parent = models.ForeignKey('self',null=True,blank=True, related_name='replies', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
    def is_reply(self):
        return self.parent is not None
