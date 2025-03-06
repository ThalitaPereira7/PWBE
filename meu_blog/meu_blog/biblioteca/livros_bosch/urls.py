from django.urls import path
from . import views

urlpatterns = [
    path('', views.livro_read, name='item_read'),
    path('novo/', views.livro_create, name='item_create'),
    path('edit/<int:pk>', views.livro_update, name='item_uptade'),
    path('delete/<int:pk>', views.livro_delete, name='item_delete')
]