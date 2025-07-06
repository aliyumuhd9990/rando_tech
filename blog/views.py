from django.shortcuts import render, redirect, get_object_or_404
from .models import *

app_name= 'blog'

# Create your views here.
def PostListView(request):
    posts = Post.published.all()
    categories = Category.objects.all()

    
    context = {
        'post' : posts,
        'category' : categories,
    }
    return render(request, 'blog/post_list.html', context)

def PostDetailView(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                            )
    
    context = {
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)