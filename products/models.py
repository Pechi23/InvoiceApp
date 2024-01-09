from django.db import models
from django.utils.text import slugify
import random

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, null=True, blank=True)
    price = models.FloatField()

    slug = models.SlugField(null=True, blank=True)
    
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slugify(self.name + str(random.randint(10000,99999))) 
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
