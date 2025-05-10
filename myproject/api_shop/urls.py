from .views import *
from rest_framework import routers

urlspatterns = [

]

router = routers.SimpleRouter()
router.register('clients', ClientsViewset, basename='clients')
router.register('manufacturers', ManufacturerViewset, basename='manufacturers')
router.register('categories', CategoryViewset, basename='categories')
router.register('animals', AnimalsViewset, basename='animals')
router.register('products', ProductsViewset, basename='products')
router.register('order_stats', OrderStatViewset, basename='orderstat')
router.register('orders', OrdersViewset, basename='orders')
router.register('productsinorders', ProductsInOrderViewset, basename='productsinorders')

urlspatterns +=router.urls