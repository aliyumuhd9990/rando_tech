from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
    path('post_list/', PostListView, name='post_list'),
    path('post_list_by_category/<slug:category_slug>/', PostListByCategoryView, name='post_list_by_category'),
    path('create_post/', CreatePostView, name='create_post'),
    path('post_detail/<int:year>/<int:month>/<int:day>/<slug:post>/', PostDetailView, name='post_detail'),
    path('your_post/', YourPostView, name='your_post'),
    path('edit_post/<int:year>/<int:month>/<int:day>/<slug:post>/', EditPostView, name='edit_post'),
    path('delete_post/<int:year>/<int:month>/<int:day>/<slug:post>/', DeletePostView, name='delete_post'),
    path('post-search/',  SearchView, name='post_search'),
]

