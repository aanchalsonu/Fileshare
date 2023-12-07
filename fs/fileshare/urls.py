
from django.contrib import admin
from django.urls import path
from .views import download_file, index, upload_file

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('upload/', upload_file, name='upload_file'),
    path('download/<str:pin>/', download_file, name='download_file'),
]
