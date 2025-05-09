from django.db import models

class Manufacturers(models.Model):
    ID_Manufacturer  = models.AutoField(primary_key=True)
    Manufacturer_Name  = models.CharField(max_length=150)
    def __unicode__(self):
        return u'name - %s' % (self.Manufacturer_Name)

class Animals(models.Model):
    ID_Animal  = models.AutoField(primary_key=True)
    Animal_Name  = models.CharField(max_length=30)
    def __unicode__(self):
        return u'name - %s' % (self.Animal_Name)

class Categories(models.Model):
    ID_Category  = models.AutoField(primary_key=True)
    Category_Name  = models.CharField(max_length=100)
    def __unicode__(self):
        return u'name - %s' % (self.Category_Name)

class Products(models.Model):
    ID_Product  = models.AutoField(primary_key=True)
    Product_Image = models.ImageField(upload_to='images/')
    Product_Name  = models.CharField(max_length=150)
    Manufacturer_ID = models.ForeignKey(Manufacturers, on_delete=models.SET_DEFAULT, default=1)
    Animal_ID = models.ForeignKey(Animals, on_delete=models.SET_DEFAULT, default=1)
    Category_ID = models.ForeignKey(Categories, on_delete=models.SET_DEFAULT, default=1)
    Product_Price = models.IntegerField(default=0)
    Product_Info = models.CharField(max_length=500)
    def __unicode__(self):
        return u'name - %s' % (self.Product_Name)
    
class Clients(models.Model):
    ID_Client  = models.AutoField(primary_key=True)
    Client_Login  = models.CharField(max_length=50)
    Client_Password  = models.CharField(max_length=50)
    Client_Second_Name  = models.CharField(max_length=100)
    Client_First_Name  = models.CharField(max_length=100)
    Client_Third_Name  = models.CharField(max_length=100)
    Client_Email  = models.CharField(max_length=150)
    Client_Phone  = models.CharField(max_length=12)
    def __unicode__(self):
        return u'login - %s, secondname - %s, name - %s' % (self.Client_Login, self.Client_Second_Name, self.Client_First_Name)
    
class Order_Statuses(models.Model):
    ID_Status  = models.AutoField(primary_key=True)
    Status_Name  = models.CharField(max_length=50)
    def __unicode__(self):
        return u'name - %s' % (self.Status_Name)

class Orders(models.Model):
    ID_Order = models.AutoField(primary_key=True)
    Client_ID = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    Status_ID = models.ForeignKey(Order_Statuses, on_delete=models.SET_DEFAULT, default=1)
    def __unicode__(self):
        return u'order number - %s' % (self.ID_Order)

class ProductsInOrders(models.Model):
    Order_ID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

class ShoppingCart(models.Model):
    Client_ID = models.ForeignKey(Clients, null=True, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Cart_Buy_Check = models.BooleanField(default=True)   





