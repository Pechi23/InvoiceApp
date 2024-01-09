from django.shortcuts import render
from .models import Invoice,InvoiceProduct
# Create your views here.

def invoices_list_view(request):
    invoices = Invoice.objects.all()
    context = {
        "invoices": invoices,
    }
    return render(request, "invoices-list.html", context=context)