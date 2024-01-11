from django.db import models
from django.conf import settings
from django.core.validators import validate_email
from django.utils.text import slugify
from clients.models import Client
from products.models import Product
from uuid import uuid4
from django.utils.timezone import now

USER = settings.AUTH_USER_MODEL

class Invoice(models.Model):
    curencies ={
        '$':'USD',
        '€':'EUR',
        '£': 'GBP',
        'RON':'RON',
    }

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.CharField(max_length=32, null=True, blank=True)
    currency = models.CharField(choices=curencies, max_length=16)

    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    @property
    def total_price(self):
        total = sum(invoice_product.partial_price for invoice_product in InvoiceProduct.objects.filter(invoice=self))
        return round(total, 2)
    
    @property
    def taxes(self):
        return round(self.total_price * 19 / 100, 2)

    
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.number = f"INV-{str(uuid4()).split('-')[3]}"
            self.slug = slugify(self.number) 
        super().save(*args,**kwargs)

    def __str__(self):
        return self.number

class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    slug = models.SlugField(max_length=64, null=True, blank=True)
    
    @property
    def partial_price(self):
        partial = self.product.price * self.quantity
        return round(partial, 2)
    
    @property
    def tax(self):
        return round(self.partial_price * 19 / 100, 2)
    
    def __str__(self):
        return f"{self.product.name}-{self.quantity}"
    
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slugify(str(uuid4()).split('-')[4])
        super().save(*args,**kwargs)
    
    

