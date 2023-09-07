from rest_framework import serializers
from.models import*
from django.contrib.auth.models import User


class signupser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class C_prodSer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProduct
        fields="__all__"

class InventorySerializer(serializers.ModelSerializer):
    
    remaining_quantity=serializers.CharField(read_only=True)
    class Meta:
        model = Inventory
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser']