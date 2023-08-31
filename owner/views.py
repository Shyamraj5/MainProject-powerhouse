from django.shortcuts import render
from.serializers import *
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import  status
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.
class SignUpView(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=signupser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"OK"})
        return Response(data=ser.errors)
    
class C_ProductModelViewset(ModelViewSet):
    serializer_class=C_prodSer
    queryset=CustomerProduct.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]