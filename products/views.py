from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

def products_list_view(request):
    form = ProductForm(request.POST or None)
    products = Product.objects.all()

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProductForm()

    context = {
        "products": products,
        "form": form,
    }

    return render(request, "products/products-list.html", context=context)
