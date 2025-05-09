from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS
from .models import Disciplina, ReservaAmbiente
from rest_framework.permissions import IsAdminUser
from rest_framework import response
from rest_framework.decorators import APIView

class GestorAutenticado(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.usuario == 'gest'


class ProfessorAutenticado(BasePermission):
    def has_permission(sel, request, view):
        return request.user.is_autheticated and request.user.usuario == 'prof'
    
class Permissao(BasePermission):    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.usuario in ['gest', 'prof']  # professor e gestor tem acesso para listar
        return request.user.usuario == 'gest'
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.usuario == 'gest':
                return True
            return request.user == obj.professor_responsavel.user
        return request.user.usuario == 'gest'
