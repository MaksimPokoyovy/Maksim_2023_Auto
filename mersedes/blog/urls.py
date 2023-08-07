from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search_results, name='search_results'),
    path('category/<str:category>/', views.blog_category, name='blog_category')
]