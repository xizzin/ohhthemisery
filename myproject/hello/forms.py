from django import forms
from .models import Clients
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import forms 
class RegistrationForm(UserCreationForm):
    Client_Username = forms.CharField(
        label = 'Логин пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    Client_Password = forms.CharField(
        label = 'Пароль пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    Client_Second_Name = forms.CharField(
        label = 'Фамилия пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    Client_First_Name = forms.CharField(
        label = 'Имя пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    Client_Third_Name = forms.CharField(
        label = 'Отчество пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    ) 
    Client_Email = forms.CharField(
        label = 'Почта пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    Client_Phone = forms.CharField(
        label = 'Почта пользователя',
        widget = forms.IntegerInput(attr={'class': 'form-control'}),
        min_length = 2
    )

    class Meta:
        model = User
        fields = ['Cient_Username', 'Client_Password', 'Client_Second_Name', 'Client_First_Name', 'Client_Third_Name', 'Client_Email', 'Client_Phone']

class LoginForm(AuthenticationForm):
    Client_Username = forms.CharField(
        label = 'Логин пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    Client_Password = forms.CharField(
        label = 'Пароль пользователя',
        widget = forms.TextInput(attr={'class': 'form-control'}),
        min_length = 2
    )
    
class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['Client_Login', 'Client_Password', 'Client_Second_Name', 'Client_First_Name', 'Client_Third_Name', 'Client_Email', 'Client_Phone']
        widgets = {
            'Client_Login':forms.TextInput(attrs={'class': 'form-control'}), 
            'Client_Password':forms.TextInput(attrs={'class': 'form-control'}), 
            'Client_Second_Name':forms.TextInput(attrs={'class': 'form-control'}), 
            'Client_First_Name':forms.TextInput(attrs={'class': 'form-control'}), 
            'Client_Third_Name':forms.TextInput(attrs={'class': 'form-control'}), 
            'Client_Email':forms.TextInput(attrs={'class': 'form-control'}), 
            'Client_Phone':forms.NumberInput(attrs={'class': 'form-control'})
        }