from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('allbooks/', views.allbooks, name='allbooks'),
    path('allbooks_sorted', views.SortedBooks.as_view(), name='allbooks_sorted'),
    path('allbooks/search/', views.SearchResultsView.as_view(), name='search_results'),
    path('allbooks/search_id/', views.BooksByAuthorId.as_view(), name='search_id_results'),
    path('add_book', views.add_book, name='add_book'),
    path('add_book/<int:id>', views.add_book, name='update_book'),
    path('allbooks/<int:pk>/', views.ID_BookView.as_view(), name='id_book'),
]