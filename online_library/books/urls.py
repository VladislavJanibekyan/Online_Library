from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="books_home"),
    path('about/', views.about, name="about"),
    path('book_view/<int:pk>', views.book_view, name="book_view"),
]