from django.shortcuts import render, redirect

app_name = 'core'


# Create your views here.
def IndexView(request):
    return render(request,'core/index.html')