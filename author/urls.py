from django.urls import path

from . import views

app_name = 'author'
urlpatterns = [
    # path('', views.index, name='index'),
    path('all_authors', views.all_authors, name='all_authors'),
    path('add_author', views.add_author, name='add_author'),
    path('add_author/<int:id>', views.add_author, name='update_author'),
]