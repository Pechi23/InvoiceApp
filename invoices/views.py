from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice,InvoiceProduct
from .forms import InvoiceForm, InvoiceProductForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def invoices_list_view(request):
    form = InvoiceForm(request.POST or None)
    invoices = Invoice.objects.all()

    if form.is_valid():
        obj = form.save()
        return redirect(f"/invoices/{obj.slug}")

    context = {
        "invoices": invoices,
        "form": form,
    }

    return render(request, "invoices/invoices-list.html", context=context)

@login_required
def invoice_edit_view(request, slug=None):
    invoice = get_object_or_404(Invoice, slug=slug)
    invoice_products = InvoiceProduct.objects.filter(invoice=invoice)

    form = InvoiceForm(request.POST or None, instance=invoice)

    if form.is_valid():
        obj = form.save()

    context = {
        "invoice": invoice,
        "invoice_products": invoice_products,
        "form": form,
    }

    return render(request, "invoices/invoice.html", context=context)

@login_required
def invoice_add_view(request, slug=None):
    invoice = get_object_or_404(Invoice, slug=slug)
    form = InvoiceProductForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.invoice = invoice
        obj.save()
        return redirect(f"/invoices/{slug}")

    context = {
        "invoice": invoice,
        "form": form,
    }

    return render(request, "invoices/add-products-to-invoice.html", context=context)

@login_required
def invoice_delete_view(request, slug=None):
    invoice = get_object_or_404(Invoice, slug=slug)

    if request.method == 'POST':
        invoice.delete()
        return redirect("/invoices/")

    context = {
        "invoice": invoice,
    }

    return render(request, "invoices/invoice-delete.html", context=context)

@login_required
def invoice_product_delete_view(request, invoice_slug=None, invoice_product_slug=None):
    invoice = get_object_or_404(Invoice, slug=invoice_slug)

    invoice_product = get_object_or_404(InvoiceProduct, invoice=invoice, slug=invoice_product_slug)


    if request.method == 'POST':
        invoice_product.delete()
        return redirect(f"/invoices/{invoice_slug}")

    context = {
        "invoice": invoice,
        "invoice_product": invoice_product,
    }

    return render(request, "invoices/invoice-product-delete.html", context=context)