from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('breathe', views.breathe),
    path('entr', views.entr),
    path('reg', views.reg),
    path('nature', views.nature),
    path('space', views.space),
    path('asmr', views.asmr),
    path('lofi', views.lofi),
    path('whitenoise', views.whitenoise),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)