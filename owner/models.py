from django.db import models
from owner.models import *
from django.contrib.auth.models import User

# Create your models here.
class CustomerProduct(models.Model):
    options={
        ('Tubular','Tubular'),
        ('Automotive','Automotive'),
        ('Inverter','Inverter'),
        }
   
    category=models.CharField(max_length=100,choices=options)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField(null=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)




class Inventory(models.Model):
    product = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField(default=0)
    sold_quantity = models.PositiveIntegerField(default=0)
    remaining_quantity = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.remaining_quantity = self.stock_quantity - self.sold_quantity
        super(Inventory, self).save(*args, **kwargs)

