from django.shortcuts import render, redirect

from .models import Order
from .forms import OrderCreateForm, OrderUpdateForm


# Create your views here.

def all_orders(request):
    order_objects = Order.objects.all()
    context = {'order_objects': order_objects}
    return render(request, 'order/all_orders.html', context)

def add_order(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = OrderCreateForm()
            submit = "Create order"
        else:
            order = Order.objects.get(pk=id)
            form = OrderUpdateForm(instance=order)
            submit = "Update"
        context = {'form': form,
                   'submit': submit}
        return render(request, 'order/add_order.html', context)
    else:
        if id == 0:
            form = OrderCreateForm(request.POST)
            submit = "Create order"
        else:
            order = Order.objects.get(pk=id)
            form = OrderUpdateForm(request.POST, instance=order)
            submit = "Update"
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('/orders/all_orders')
        else:
            return render(request, 'order/add_order.html', {'form': form, 'submit': submit})

def ordered_orders(request):
    order_objects = Order.objects.all().order_by('created_at', 'plated_end_at')
    context = {'order_objects': order_objects}
    return render(request, 'order/ordered_orders.html', context)

def filtered_orders(request):
    order_objects = Order.objects.filter(created_at__gt='end_at')
    context = {'order_objects': order_objects}
    return render(request, 'order/ordered_orders.html', context)