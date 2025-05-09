from django.contrib import admin
from .models import Animals
from .models import Manufacturers
from .models import Categories
from .models import Products
from .models import Clients
from .models import Order_Statuses
from .models import Orders
from .models import ProductsInOrders
from .models import ShoppingCart
# Register your models here.
admin.site.register(Animals)
admin.site.register(Categories)
admin.site.register(Manufacturers)
admin.site.register(Products)
admin.site.register(Clients)
admin.site.register(ShoppingCart)
admin.site.register(Order_Statuses)
admin.site.register(Orders)
admin.site.register(ProductsInOrders)
