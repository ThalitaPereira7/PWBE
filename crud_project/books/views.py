from django.shortcuts import render, redirect, get_object_or_404
from .models import Book  # Substituir Item por Book, se necessário
from .form import BookForm  # Substituir ItemForm por BookForm, se necessário

# Visualizar livros cadastrados
def book_read(request):
    books = Book.objects.all()  # Alterado para Book
    return render(request, 'books/book_read.html', {'books': books})

# Cadastrar novo livro
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)  # Alterado para BookForm
        if form.is_valid():
            form.save()
            return redirect('book_read')  # Alterado para book_read
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})

# Atualizar dados do livro
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Alterado para Book
    if request.method == 'POST':  # Mudança de PUT para POST
        form = BookForm(request.POST, instance=book)  # Alterado para BookForm
        if form.is_valid():
            form.save()
            return redirect('book_read')  # Alterado para book_read
    else:
        form = BookForm(instance=book)  # Alterado para BookForm

    return render(request, 'books/book_form.html', {'form': form})

# Remover livro
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Alterado para Book
    if request.method == 'POST':
        book.delete()  # Alterado de Item.delete() para book.delete()
        return redirect('book_read')  # Alterado para book_read
    return render(request, 'books/book_delete.html', {'book': book})  # Alterado para book
