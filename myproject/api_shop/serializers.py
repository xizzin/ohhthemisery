from rest_framework import serializers
from hello.models import Categories, Clients, Orders, ProductsInOrders, Products, Manufacturers, Animals, Order_Statuses

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = {
            'Client_Login',
            'Client_Password',
            'Client_Second_Name',
            'Client_First_Name',
            'Client_Third_Name',
            'Client_Email',
            'Client_Phone'
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = {
            'Category_Name'
        }

class OrderStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Statuses
        fields = {
            'Status_Name'
        }

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = {
            'Manufacturer_Name'
        }

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = {
            'Animal_Name'
        }

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = {
            'Client_ID',
            'Status_ID'
        }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = {
            'Product_Name',
            'Manufacturer_ID',
            'Animal_ID',
            'Category_ID',
            'Product_Price',
            'Product_Info'
        }

class ProductsInOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInOrders
        fields = {
            'Order_ID',
            'Product_ID',
            'Quantity'
        }