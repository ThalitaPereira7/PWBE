from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.index),
    path('eventos/criar/', views.criar_evento),
    path('eventos/<int:pk>/', views.atualizar_evento),
    path('eventos/<int:pk>/deletar/', views.deletar_evento),
]
