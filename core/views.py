from django.shortcuts import render, redirect, get_object_or_404
from blog.models import *
from .models import *

app_name = 'core'


# Create your views here.
def IndexView(request):
    posts = Post.published.all()[:4]
    category = Category.objects.all()
    service = Service.objects.all()
    services = Service.objects.all()
    
    
    context = {
        'post' : posts,
        'category' : category,
        'service' : service,
        'services' : services,
    }
    return render(request,'core/index.html', context)

def AboutView(request):
    services = Service.objects.all()
    
    context = {
        'services' : services,
    }
    return render(request, 'core/about.html', context)
def ServicesView(request):
    services = Service.objects.all()
    service = Service.objects.all()
    
    context = {
        'service' : service,
        'services' : services,
    }
    return render(request, 'core/services.html', context)
def ContactView(request):
    services = Service.objects.all()
    
    context = {
        'services' : services,
    }
    return render(request, 'core/contact.html', context)

def ServiceDetailView(request, id):
    service = get_object_or_404(Service, id=id)
    services = Service.objects.all()
    package = Package.objects.all()
    context = {
        'service' : service,
        'services' : services,
        'package' : package,
    }
    return render(request, 'core/service_detail.html', context)

def PrivacyView(request):
    services = Service.objects.all()
    
    context = {
        'services' : services,
    }
    return render(request, 'some_pages/privacy.html', context)


def SecurityView(request):
    services = Service.objects.all()
    
    context = {
        'services' : services,
    }
    return render(request, 'some_pages/security.html', context)

def FAQView(request):
    services = Service.objects.all()
    
    context = {
        'services' : services,
    }
    return render(request, 'some_pages/faq.html', context)

def AskView(request):
    services = Service.objects.all()
    
    context = {
        'services' : services,
    }
    return render(request, 'some_pages/ask_questions.html', context)