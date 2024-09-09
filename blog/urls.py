from . import views
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_blog, name='blog_create'),
    path('search/', views.search, name='search'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('<int:blog_id>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
    path('register/', views.register, name='register'),
    
    
    
   
]