from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def home(request):
    book = Book
    return render(request, 'books/books_home.html', {'book': content})

def about(request):
    return render(request, 'books/about.html')