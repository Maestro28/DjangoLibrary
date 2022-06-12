from django.urls import path
from . import views


app_name = "author"

urlpatterns = [
    path('', views.AuthorGenerics.as_view(), name='all_authors'),
    path('<int:pk>/', views.AuthorDetailGenerics.as_view(), name='author_detail'),
]