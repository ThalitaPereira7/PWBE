from django.urls import path
from .views import create_user, logar, ver_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path('cadastro/', create_user, name='cadastro'),
    path('login/', logar, name='login'),
    path('me/', ver_usuario, name='ver_usuario'),
    path('atualizar/', atualizar_usuario, name='atualizar_usuario'),
    path('deletar/', deletar_usuario, name='deletar_usuario'),
]
