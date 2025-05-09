from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from .serializers import *
from .models import Professor, Disciplina, ReservaAmbiente, Usuario
from .permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView




#PROFESSORES

#Lista e Cria os Professores
class ProfessorListCreateAPIView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [GestorAutenticado]

    def get_queryset(self): # Permitir a filtragem dos resultados com base no parâmetro de consulta nome
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset



#Edita, atualiza e exclui algo especifico pela chave primaria
class ProfessorRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'pk'
    permission_classes = [GestorAutenticado]

#Exclui (ainda preciso ve se o de cima ja faz isso :) ! )
class ProfessorDeleteAPIView(DestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
#DISCIPLINAS

class DisciplinaListCreateAPIView(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [GestorAutenticado]

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    


class DisciplinaRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    lookup_field = 'pk'
    permission_classes = [Permissao]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [Permissao()]
        return [GestorAutenticado()]


#AMBIENTES

class ReservasListCreateAPIView(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [GestorAutenticado]

    def get_queryset(self):
        queryset = super().get_queryset()
        sala_reservada = self.request.query_params.get('sala_reservada')
        if sala_reservada:
            queryset.filter(nome__icontains=sala_reservada)
        return queryset

class ReservasRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    lookup_field = 'pk'
    permission_classes = [Permissao]

    def get_permissions(self): # gerenciando as permissões
        if self.request.method == 'GET':
            return [Permissao()]
        return [GestorAutenticado()]

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

    
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer



