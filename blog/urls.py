from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
    path('post_list/', PostListView, name='post_list'),
    path('post_detail/<int:year>/<int:month>/<int:day>/<slug:post>/', PostDetailView, name='post_detail'),
]

