from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    book = Book.objects.all()

    return render(request, 'books/books_home.html', {'books': book })

def about(request):
    return render(request, 'books/about.html')
@login_required
def book_view(request, pk):
    specific_book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_view.html', {'book': specific_book})