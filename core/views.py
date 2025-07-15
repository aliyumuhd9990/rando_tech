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

def AboutView(request):
    return render(request, 'core/about.html')
def ServicesView(request):
    return render(request, 'core/services.html')
def ContactView(request):
    return render(request, 'core/contact.html')