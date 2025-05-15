from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Disciplina, ReservaAmbiente, Usuario
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    lookup_field = 'pk'
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return[IsAuthenticated()]
        return[IsAdminUser(), IsAuthenticated()]
    
class DisciplinaListCreateView(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

class DisciplinaRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser, IsAuthenticated]

class ReservaListCreateView(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

class ReservaRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser, IsAuthenticated]

class ProfDisciplinasListView(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(professor_responsavel=self.request.user.pk)

class ProfReservaListView(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(professor_responsavel=self.request.user.pk)