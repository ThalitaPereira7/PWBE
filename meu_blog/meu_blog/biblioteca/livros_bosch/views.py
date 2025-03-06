from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .form import LivroForm
# Create your views here.

def livro_read(request):
    items = Livro.objects.all()
    return render(request, "item_read.html", {'items':items})

def livro_create(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = LivroForm()

    return render(request, 'item_form.html', {'form': form})

def livro_update(request, pk):
    item = get_object_or_404(Livro, pk=pk)
    if request.method == 'PUT':
        form = LivroForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = LivroForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def livro_delete(request, pk):
    item = get_object_or_404(Livro, pk)
    if request.method == 'POST':
        Livro.delete()
        return redirect('item_read')
    return render(request, 'item_confirm_delete.html' , {'item': item})