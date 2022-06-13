from django.urls import include, path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:authentication:all_users', request=request, format=format),
        'orders': reverse('api:order:all_orders', request=request, format=format),
        'authors': reverse('api:author:all_authors', request=request, format=format),
        'books': reverse('api:book:all_books', request=request, format=format),
    })


urlpatterns = [
    path('', api_root, name='root'),
    path('v1/user/', include('authentication.rest.urls', namespace="authentication")),
    path('v1/order/', include('order.rest.urls', namespace="order")),
    path('v1/author/', include('author.rest.urls', namespace="author")),
    path('v1/book/', include('book.rest.urls', namespace="book")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
