from django.shortcuts import render, redirect
from blog.models import *

app_name = 'core'


# Create your views here.
def IndexView(request):
    posts = Post.published.all()[:3]
    
    context = {
        'post' : posts,
    }
    return render(request,'core/index.html', context)