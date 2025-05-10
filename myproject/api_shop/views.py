from django.shortcuts import render
from rest_framework import viewsets
from hello.models import *
from .serializers import *
from permissions import *

class ClientsViewset(viewsets.ModelViewSet):
    queryset = Clients.objects.all
    serializer_class = ClientSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class AnimalsViewset(viewsets.ModelViewSet):
    queryset = Animals.objects.all
    serializer_class = AnimalSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ManufacturerViewset(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all
    serializer_class = ManufacturerSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderStatViewset(viewsets.ModelViewSet):
    queryset = Order_Statuses.objects.all
    serializer_class = OrderStatSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ProductsInOrderViewset(viewsets.ModelViewSet):
    queryset = ProductsInOrders.objects.all
    serializer_class = ProductsInOrdersSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage