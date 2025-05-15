from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns= [

    path('login/', LoginView.as_view(), name='login'),

    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetriveUpdateDestroyView.as_view(), name='usuario-retrieve-update-destroy'),
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaRetriveUpdateDestroyView.as_view(), name='disciplina-retrieve-update-destroy'),
    path('reservas/', ReservaListCreateView.as_view(), name='reservas-list-create'),
    path('reservas/<int:pk>/', ReservaRetriveUpdateDestroyView.as_view(), name='reservas-retrieve-update-destroy'),
    path('reserva_prof/disciplinas/', ProfDisciplinasListView.as_view(), name='reservas-disciplina-list'),    
    path('reserva_prof/salas/', ProfReservaListView.as_view(), name='reservas-sala-list'),

    path('autenticacao/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('autenticacao/refresh', TokenRefreshView.as_view(), name="token_refresh"),

]