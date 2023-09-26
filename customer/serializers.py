from rest_framework import serializers
from.models import*
from django.contrib.auth.models import User
from owner.serializers import *



class CustSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    product=C_prodSer().read_only=True
    class Meta:
        model=C_Orders
        fields = '__all__'


class getorderser(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    product=C_prodSer()
    class Meta:
        model=C_Orders
        fields = '__all__'

class complaintser(serializers.ModelSerializer):  
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=complaints
        fields="__all__"



class serviceser(serializers.ModelSerializer):  
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=services
        fields="__all__"

class itemRating(serializers.ModelSerializer):  
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Itemrating
        fields=[""]

class serviceRating(serializers.ModelSerializer):  
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Servicerating
        fields="__all__"


class complaintRating(serializers.ModelSerializer):  
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Complaintrating
        fields="__all__"


# class cartser(serializers.ModelSerializer):  
#     user=serializers.CharField(read_only=True)
  
    
    
#     class Meta:
#         model=Cart
#         fields="__all__"

class cartser(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    quantity=serializers.CharField(read_only=True)
    product=C_prodSer()
    class Meta:
        model = Cart
        fields ="__all__"