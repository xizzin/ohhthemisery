from django import forms
from .models import Clients

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