from django.urls import path
from . import views


app_name = "authentication"

urlpatterns = [
    path('', views.CustomUserGenerics.as_view(), name='all_users'),
    path('<int:pk>/', views.CustomUserDetailGenerics.as_view(), name='user_detail'),
    path('<int:user_id>/order/<int:id>', views.UserOrderDetailGenerics.as_view(), name='user_order_detail')
]
