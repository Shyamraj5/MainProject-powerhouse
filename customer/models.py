from django.db import models
from owner.models import *
from django.contrib.auth.models import User
# Create your models here.



class Cart(models.Model):
    product = models.ForeignKey(CustomerProduct, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    
class C_Orders(models.Model):
    product=models.ForeignKey(CustomerProduct,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=500)
    phone=models.IntegerField()
    date=models.DateField(auto_now_add=True,null=True)




    

    
    @property
    def totalamt(self):
        cnt=self.product.price*self.quantity
        return cnt 
    



class complaints(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)
    place=models.CharField(max_length=200)
    phone=models.IntegerField()


class services(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    place=models.CharField(max_length=100,null=True)
    phone=models.IntegerField(null=True)
    

class Itemrating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(C_Orders,on_delete=models.CASCADE,null=True)
    rating = models.PositiveIntegerField()


class Complaintrating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    complaint = models.ForeignKey(complaints,on_delete=models.CASCADE,null=True)
    rating = models.PositiveIntegerField()


class Servicerating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(services,on_delete=models.CASCADE,null=True)
    rating = models.PositiveIntegerField()


class AdminResponse(models.Model):

   
    options = (
        ('thank you for your response', 'thank you for your response'),
        ('service engineer on the way', 'service engineer on the way'),
        ('having some delay come after a day', 'having some delay come after a day'),
    )
    response = models.CharField(max_length=500, choices=options)
   
    service = models.ForeignKey(services, on_delete=models.CASCADE,null=True)
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)