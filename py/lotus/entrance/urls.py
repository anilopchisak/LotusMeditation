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
    path('nature', views.nature),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)