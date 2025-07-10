from django.shortcuts import render, redirect
from blog.models import *

app_name = 'core'


# Create your views here.
def IndexView(request):
    posts = Post.published.all()[:3]
    category = Category.objects.all()
    
    context = {
        'post' : posts,
        'category' : category,
    }
    return render(request,'core/index.html', context)