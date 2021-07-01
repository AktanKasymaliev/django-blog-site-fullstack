from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static
from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blogs.urls")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('api.urls'))
]

handler404 = 'blogs.responses.handlers.handler404'
handler500 = 'blogs.responses.handlers.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
    urlpatterns += url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), 
