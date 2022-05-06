from django.shortcuts import render
from order.models import Order

# Create your views here.

def all_orders(request):
    order_objects = Order.objects.all()
    context = {'order_objects': order_objects}
    return render(request, 'order/all_orders.html', context)

def ordered_orders(request):
    order_objects = Order.objects.all().order_by('created_at', 'plated_end_at')
    context = {'order_objects': order_objects}
    return render(request, 'order/ordered_orders.html', context)

def filtered_orders(request):
    order_objects = Order.objects.filter(created_at__gt='end_at')
    context = {'order_objects': order_objects}
    return render(request, 'order/ordered_orders.html', context)