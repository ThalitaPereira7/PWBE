from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Evento
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    evento = Evento.objects.all()

    categoria = request.GET.get('categoria')
    if categoria:
        evento = evento.filter(categoria__iexact=categoria) 

    data = request.GET.get('data')
    if data:
        evento = evento.filter(data_hora__date=data) 

    quantidade = request.GET.get('quantidade')
    if quantidade and quantidade.isdigit():
        evento = evento[:int(quantidade)]

    # Ordenação
    ordering = request.GET.get('ordering')
    if ordering == 'data':
        evento = evento.order_by('data_hora')

    serializer = EventoSerializer(evento, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_evento(request):
    serializer = EventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    evento.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
