from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('allbooks', views.allbooks, name='allbooks'),
    path('allbooks/search/', views.SearchResultsView.as_view(), name='search_results'),
    path('add_book', views.add_book, name='add_book'),
    path('add_book/<int:id>', views.add_book, name='update_book'),
    path('allbooks/<int:pk>/', views.ID_BookView.as_view(), name='id_book'),
    path('allbooks/filters/', views.filtered_books, name='filtered_books'),
    path('allbooks/order_by_count_asc/', views.ordered_books_count_ascending, name='ordered_books_count_ascending'),
    path('allbooks/order_by_count_dsc/', views.ordered_books_count_descending, name='ordered_books_count_descending'),
    path('allbooks/order_by_name_asc/', views.ordered_books_name_ascending, name='ordered_books_name_ascending'),
    path('allbooks/order_by_name_dsc/', views.ordered_books_name_descending, name='ordered_books_name_descending'),
]