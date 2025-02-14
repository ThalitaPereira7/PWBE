from django.shortcuts import render
from .models import Lista

def lista_tarefas(request):
    lista = Lista.objects.all().order_by('-data')
    return render(request, 'list/lista_tarefas.html', {'lista': lista})

# Create your views here.
