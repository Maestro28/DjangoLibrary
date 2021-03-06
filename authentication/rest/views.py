from rest_framework import generics
from rest_framework.generics import get_object_or_404
from order.models import Order
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, UserOrderDetailSerializer
from authentication.models import CustomUser
from .permissions import IsAdmOrIsOwnerOrReadOnly


class CustomUserGenerics(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer

    permission_classes = [IsAdmOrIsOwnerOrReadOnly]


class UserOrderDetailGenerics(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = UserOrderDetailSerializer
    multiple_lookup_fields = ('user_id', 'id')

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


