from django.contrib import admin
from .models import *

# Register your models here.
# Change site header, title, and index title
admin.site.site_header = "RandoTech"
admin.site.site_title = "RandoTech Admin Page"
admin.site.index_title = "Welcome to RandoTech Admin Dashboard"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price1', 'price2', 'price3']
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ['name', 'memail', 'msg']

