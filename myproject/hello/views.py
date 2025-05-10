from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/auth.html', context)

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'auth/registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')

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
