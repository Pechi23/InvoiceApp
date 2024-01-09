from django.db import models
from django.conf import settings
from django.core.validators import validate_email
from django.utils.text import slugify
import random

USER = settings.AUTH_USER_MODEL

class Client(models.Model):
    user = models.ForeignKey(USER, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256,validators=[validate_email])

    slug = models.SlugField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slugify(self.full_name + str(random.randint(10000,99999))) 
        super().save(*args,**kwargs)

    def __str__(self):
        return self.full_name
    
