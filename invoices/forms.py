from django import forms
from .models import *

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ["client", "currency"]

class InvoiceProductForm(forms.ModelForm):
    class Meta:
        model = InvoiceProduct
        fields = ["product", "quantity"]