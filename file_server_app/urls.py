from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('create-file/', views.create_file, name='create_file'),
    path('get-files/', views.get_files, name='get_files'),
    path('get-file/<str:filename>/', views.get_file, name='get_file'),
    path('update-file/<str:filename>/', views.update_file, name='update_file'),
    path('delete-file/<str:filename>/', views.delete_file, name='delete_file'),
    path('download_file/<str:filename>/', views.download_file, name='download_file'),
    path('home/',views.home,name='home'),
    path('',views.homepage,name='homepage'),
    path('getfiles/',views.getdata,name='getfiles')
    # Define other URL patterns as needed
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)