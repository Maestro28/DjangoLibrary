from django.shortcuts import render, redirect
from django.views import generic
import datetime

from .models import Order
from .forms import OrderCreateForm, OrderUpdateForm , SortForm


# Create your views here.

def all_orders(request):
    # order_objects = Order.objects.all()
    if request.user.is_admin:
        in_progress_orders = Order.objects.filter(end_at__isnull=True)
        closed_orders = Order.objects.filter(end_at__isnull=False)
    else:
        in_progress_orders = Order.objects.filter(end_at__isnull=True, user=request.user)
        closed_orders = Order.objects.filter(end_at__isnull=False, user=request.user)

    query = request.GET.get("sort_field")
    if query:
        in_progress_orders = in_progress_orders.order_by(query)
        closed_orders = closed_orders.order_by(query)

    # context = {'order_objects': order_objects}
    sort_form = SortForm()
    context = {
        'in_progress_orders': in_progress_orders,
        'closed_orders': closed_orders,
        'sort_form': sort_form,
    }
    return render(request, 'order/all_orders.html', context)

def add_order(request, id=0):
    if request.method == "GET":
        if id == 0:
            planed_date = datetime.datetime.now() + datetime.timedelta(days=5)
            planed_date = planed_date.strftime("%Y-%m-%d")
            form = OrderCreateForm(initial={'plated_end_at': planed_date})
            submit = "Create order"
        else:
            order = Order.objects.get(pk=id)
            form = OrderUpdateForm(instance=order, initial={'end_at': datetime.datetime.now()})
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
            submit = "Close"
        if form.is_valid():
            order = form.save(commit=False)
            # change book count
            book = order.book
            if submit == "Close":
                book.count += 1
            else:
                if book.count == 0:
                    return render(request, 'order/add_order.html', {'form': form,
                                                                    'submit': submit,
                                                                    'no_book': book.name
                                                                    })
                book.count -= 1
            book.save()

            order.user = request.user
            order.save()
            return redirect('/orders/all_orders')
        else:
            return render(request, 'order/add_order.html', {'form': form, 'submit': submit})
