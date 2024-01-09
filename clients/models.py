from django.db import models
from django.conf import settings
from django.core.validators import validate_email
from django.utils.text import slugify
from uuid import uuid4

USER = settings.AUTH_USER_MODEL

class Client(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256,validators=[validate_email])

    UniqueId = models.CharField(max_length=16, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self,*args,**kwargs):
        if self.UniqueId is None:
            self.UniqueId = str(uuid4()).split('-')[3]
            self.slug = slugify(self.full_name + self.UniqueId) 
        super().save(*args,**kwargs)
    
