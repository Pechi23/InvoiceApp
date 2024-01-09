from django.db import models
from django.utils.text import slugify
from uuid import uuid4

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)
    price = models.PositiveIntegerField()

    UniqueId = models.CharField(max_length=16)
    slug = models.SlugField()
    
    def save(self,*args,**kwargs):
        if self.UniqueId is None:
            self.UniqueId = str(uuid4).split('-')[4]
            self.slug = slugify(self.full_name + self.UniqueId) 
        super().save(*args,**kwargs)
    
