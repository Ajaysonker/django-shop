from django import forms
from phonenumber_field import widgets
from django.utils.translation import ugettext_lazy as _
from .models import Customer, Order, ProductInOrder


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email', 'address']
        labels = {
            'first_name': _("Ім'я"),
            'last_name': _("Фамілія"),
            'phone': _("Телефон"),
            'email': _("Email"),
            'address': _("Адреса"),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': "inputFirst_name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': "inputLast_name"}),
            'phone': widgets.TextInput(attrs={'class': 'form-control', 'id': "inputPhone"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': "inputEmail"}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'id': "inputAddress", 'rows': 1}),
        }


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['comment']
        labels = {
            'comment': _("Ваш коментар"),
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'id': "Textarea1", 'rows': 3}),
        }
