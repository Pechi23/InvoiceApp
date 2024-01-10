from django import forms
from .models import *

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ["client", "currency"]

#     def clean(self):
#         data = self.cleaned_data

#         client = data.get("client")
#         user = client.user
#         qs = Invoice.objects.filter(client=client).filter(client__user=user)

#         if client not in self.client_set():
#             self.add_error("client", f"\"{client.full_name}\" is not registered as your client")

#         return data

class InvoiceProductForm(forms.ModelForm):
    class Meta:
        model = InvoiceProduct
        fields = ["product", "quantity"]