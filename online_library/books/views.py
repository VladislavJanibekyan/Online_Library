from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import DropdownForm
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

class AdvancedSearch(ListView):
    model = Book
    template_name = 'books/advanced_search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains= query) )

        return object_list



def home(request):
    book = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(book, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'books/books_home.html', {'books': book[1:6]})
def rate_1(request, rate,pk):
    book = Book.objects.all()
    if request.method =="GET":
        specific_book = get_object_or_404(Book, pk=pk)
        specific_book.rate_times += 1
        specific_book.rate += rate
        specific_book.rate_total = specific_book.rate / specific_book.rate_times
        specific_book.save()


    return render(request, 'books/books_home.html', {'books': book[1:6]})

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
        specific_book.downloaded_times += 1
        specific_book.save()
        user_profile = get_object_or_404(UserProfile, id=request.user.userprofile.id)
        user_profile.books.add(specific_book)
        user_profile.save()
    return render(request, 'books/book_download.html', {'book': specific_book})

@login_required()
def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf_file')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

class CategoryView(ListView):
    model = Book
    template_name = 'books/category.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(category=query)
        )
        return object_list

