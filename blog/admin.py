from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title','slug', 'author', 'publish', 'status')
    list_filter = ('status','created', 'publish', 'author')
    raw_id_fields = ('author',)
    search_fields = ('title','body')
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    
    