from django.contrib import admin
from .models import *
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    list_display = ["number", "UniqueId", "total_price"]

admin.site.register(Invoice, InvoiceAdmin)

class InvoiceProductAdmin(admin.ModelAdmin):
    model = InvoiceProduct
    list_display = ["invoice", "product", "quantity", "partial_price"]

admin.site.register(InvoiceProduct, InvoiceProductAdmin)

