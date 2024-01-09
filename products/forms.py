from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]

    def clean(self):
        data = self.cleaned_data

        name = data.get("name")
        qs_name = Product.objects.filter(name__iexact=name)
        if qs_name.exists():
            self.add_error("name", f"\"{name}\" is already registered as a product")

        price = data.get("price")
        if price <= 0 or price >= 10000000:
            self.add_error("price", "Price cannot be less or equal than zero or bigger that 10000000")

        return data