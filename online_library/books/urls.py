from django.urls import path
from . import views
from .views import  SearchResultsView, AdvancedSearch


urlpatterns =[
    path('', views.home, name="books_home"),
    path('rating_1/<int:rate>/<int:pk>', views.rate_1, name="rate_1"),
    path('about/', views.about, name="about"),
    path('book_view/<int:pk>', views.book_view, name="book_view"),
    path('book_download/<int:pk>', views.book_download, name="book_download"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('advanced/', AdvancedSearch.as_view(), name='advanced_search'),

]