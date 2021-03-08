from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import DropdownForm
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from registration.models import UserProfile
from django.contrib import messages



class SearchResultsView(ListView):
    model = Book
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        query1 =self.request.GET.get("age_group")
        print(self.request.GET, query1)
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)| Q(author__icontains=query)| Q(language__icontains=query)| Q(publish_year__icontains=query) | Q(age_group=query1)
        )
        return object_list


def home(request):
    book = Book.objects.all()
    form = DropdownForm()

    return render(request, 'books/books_home.html', {'books': book, "form": form})

def about(request):
    return render(request, 'books/about.html')

@login_required
def book_view(request, pk):
    specific_book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_view.html', {'book': specific_book})
@login_required
def book_download(request, pk):
    specific_book = get_object_or_404(Book, pk=pk)

    if request.method == "GET":

        user_profile = get_object_or_404(UserProfile, id=request.user.userprofile.id)
        user_profile.books.add(specific_book)
        user_profile.save()
    return render(request, 'books/book_download.html', {'book': specific_book})

