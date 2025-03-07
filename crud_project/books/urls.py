from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_read, name='book_read'),  
    path('novo/', views.book_create, name='book_create'),  
    path('edit/<int:pk>/', views.book_update, name='book_update'),  
    path('delete/<int:pk>/', views.book_delete, name='book_delete'), 
]
