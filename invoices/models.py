from django.db import models
from django.conf import settings
from django.core.validators import validate_email
from django.utils.text import slugify
from clients.models import Client
from products.models import Product
from uuid import uuid4

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

    UniqueId = models.CharField(max_length=32,blank=True,null=True)
    slug = models.SlugField(null=True, blank=True)

    @property
    def total_price(self):
        total = sum(invoice_product.partial_price for invoice_product in InvoiceProduct.objects.filter(invoice=self))
        return total

    
    def save(self,*args,**kwargs):
        if self.UniqueId is None:
            self.UniqueId = str(uuid4()).split('-')[3]
            self.number = f"INV-{self.UniqueId}"
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
        return partial
    
    def __str__(self):
        return f"{self.product.name}-{self.quantity}"
    
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.number = str(uuid4()).split('-')[4]
            self.slug = slugify(self.number) 
        super().save(*args,**kwargs)
    
    

