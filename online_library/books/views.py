from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib import messages



class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)| Q(author__icontains=query)
        )
        return object_list


def home(request):
    book = Book.objects.all()

    return render(request, 'books/books_home.html', {'books': book })

def about(request):
    return render(request, 'books/about.html')

@login_required
def book_view(request, pk):
    specific_book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_view.html', {'book': specific_book})

@login_required()
def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf_file')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404
