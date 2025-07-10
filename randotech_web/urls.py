from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#for django-jazzmin
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    # Include set_language!
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls', namespace='core')),
    path('blog/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


