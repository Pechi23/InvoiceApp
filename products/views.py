from django.shortcuts import render
from .models import Product
# Create your views here.

def products_list_view(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products-list.html", context=context)
