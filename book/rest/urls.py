from django.urls import path
from . import views


app_name = "book"

urlpatterns = [
    path('', views.BookGenerics.as_view(), name='all_books'),
    path('<int:pk>/', views.BookDetailGenerics.as_view(), name='book_detail'),
]
