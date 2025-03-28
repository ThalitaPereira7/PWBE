from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    nome = request.data.get('nome')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')  
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')

    if not username or not password or not email:
        return Response({'Erro': 'Informações insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"Erro": 'Username já existente'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"Erro": 'Email já existe'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        nome=nome,
        biografia=biografia,
        idade=idade,
        telefone=telefone,
        endereco=endereco,
        escolaridade=escolaridade,
        animais=animais
    )

    return Response({'Mensagem': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuário ou senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ver_usuario(request):
    usuario = request.user
    dados_usuario = {
        'id': usuario.id,
        'username': usuario.username,
        'email': usuario.email,
        'nome': usuario.nome,
        'biografia': usuario.biografia,
        'idade': usuario.idade,
        'telefone': usuario.telefone,
        'endereco': usuario.endereco,  
        'escolaridade': usuario.escolaridade,
        'animais': usuario.animais
    }
    return Response(dados_usuario, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar_usuario(request):
    usuario = request.user

    usuario.nome = request.data.get('nome', usuario.nome)
    usuario.biografia = request.data.get('biografia', usuario.biografia)
    usuario.idade = request.data.get('idade', usuario.idade)
    usuario.telefone = request.data.get('telefone', usuario.telefone)
    usuario.endereco = request.data.get('endereco', usuario.endereco)  
    usuario.escolaridade = request.data.get('escolaridade', usuario.escolaridade)
    usuario.animais = request.data.get('animais', usuario.animais)

    usuario.save()
    return Response({'Mensagem': 'Usuário atualizado com sucesso'}, status=status.HTTP_200_OK)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletar_usuario(request):
    usuario = request.user
    usuario.delete()
    return Response({'Mensagem': 'Usuário deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)


# Create your views here.
