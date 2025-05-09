from django.shortcuts import render
from .models import Categories
from .models import Products
from .models import Clients
from .forms import ClientForm
def index(request):
    return render(request, 'hello/index.html')

def categories(request):
    categories = Categories.objects
    products = Products.objects
    return render(request, 'hello/categories.html', {'categories' : categories, 'products' : products})

def profile(request):
    clients = Clients.objects
    form = ClientForm(request.POST or None)
    return render(request, 'hello/profile.html', {'clients':clients, 'form': form})

def shopcart(request):
    return render(request, 'hello/shopcart.html')

def productpage(request):
    categories = Categories.objects
    products = Products.objects
    return render(request, 'hello/product_page')


def result(request):
    user_filter = request.GET['ID_Category']
    mydata = Products.objects.filter(Category_ID =user_filter)
    return render(request, 'hello/allproducts.html', {'products': mydata})

def aboutus(request):
    return render(request, 'hello/aboutus.html')

def allprojects(request):
    return render(request, 'hello/allprojects_page.html')
