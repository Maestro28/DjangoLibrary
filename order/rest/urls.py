from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('', views.OrderViewSet.as_view(), name='all_orders'),
    path('<int:pk>/', views.OrderDetailViewSet.as_view(), name='order_detail')
]