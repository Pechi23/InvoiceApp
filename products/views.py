from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
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

@login_required
def product_delete_view(request, slug=None):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        product.delete()
        return redirect("/products/")

    context = {
        "product": product,
    }

    return render(request, "products/product-delete.html", context=context)
