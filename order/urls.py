from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('all_orders', views.all_orders, name='all_orders'),
    path('add_order', views.add_order, name='add_order'),
    path('add_author/<int:id>', views.add_order, name='update_order'),
]