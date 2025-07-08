from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Prefetch

app_name= 'blog'

# Create your views here.
def PostListView(request):
    posts = Post.published.all()[:4]
    categories = Category.objects.all()

    
    context = {
        'post' : posts,
        'category' : categories,
    }
    return render(request, 'blog/post_list.html', context)

@login_required
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

@login_required
def CreatePostView(request):
    category = Category.objects.all()
    
    
    if request.method == 'POST':
        category = Category.objects.all()

    if request.method == 'POST':
        post_title = request.POST.get('post_title')
        post_body = request.POST.get('post_body')
        post_cover = request.FILES.get('post_cover')
        post_category_id = request.POST.get('cat')
        slug=slugify(post_title)
        
        category = Category.objects.get(id=post_category_id)

        post = Post.objects.create(
            author=request.user,
            title=post_title,
            body=post_body,
            cover_img=post_cover,
            category=category,
            slug=slug,
        )

        
        post.save()
        messages.success(request, 'Post successfully created')
        return redirect('blog:create_post')
    
    context = {
        'category' : category,
    }
    return render(request, 'blog/create_post.html', context)

def YourPostView(request):
    post = Post.objects.filter(author=request.user)
    # Get all unique category names for posts by this user
    user_categories = Category.objects.filter(
        category_post__author=request.user
    ).distinct()

    # Or if you only want names as a list:
    category_names = user_categories.values_list('name', flat=True)
    
    context = {
        'post' : post,
        'category' : category_names,
    }
    return render(request, 'blog/your_post.html', context)