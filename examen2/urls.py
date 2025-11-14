from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('movies.urls', 'movies'), namespace='movies')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
