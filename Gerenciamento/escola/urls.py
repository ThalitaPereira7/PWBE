from .views import *
from django.urls import path

urlpatterns= [
    path('login/', LoginView.as_view(), name='logar'),
    
    path('professor/', ProfessorListCreateAPIView.as_view(), name='professor-list-create'),
    path('professor/<int:pk>/', ProfessorRetriveUpdateDestroyAPIView.as_view(), name = 'professor-Retrieve-Update-Destroy'),

    path('disciplinas/', DisciplinaListCreateAPIView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaRetriveUpdateDestroyAPIView.as_view(), name='disciplina-detail'),

    path('reservas/', ReservasListCreateAPIView.as_view(), name='reserva-list-create'),
    path('reservas/<int:pk>/', ReservasRetriveUpdateDestroyAPIView.as_view(), name='reserva-detail'),
]