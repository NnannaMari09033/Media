
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

from django.urls import path


urlpatterns = [
    path('index/', views.home, name='index'),
    path('debug/', views.debug_template_path, name='debug'),
    path('download/<str:filename>/', views.download_file, name='download')
]

