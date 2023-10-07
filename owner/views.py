from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import authentication, permissions
from customer.serializers import*
# Create your views here.
# class SignUpView(ViewSet):
#     def create(self,request,*args,**kwargs):
#         ser=signupser(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({"msg":"OK"})
#         return Response(data=ser.errors)



        
class SignUpView(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=signupser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"OK"})
        return Response(data=ser.errors)


class C_ProductModelViewset(ModelViewSet):
    serializer_class = C_prodSer
    queryset = CustomerProduct.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def destroy(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            CustomerProduct.objects.filter(id=id).delete()
            return Response({"msg":"Deleted"})


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class getallservice(ModelViewSet):
    serializer_class=serviceser
    queryset=services.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return services.objects.all()
    
class getallcomp(ModelViewSet):
    serializer_class=complaintser
    queryset=complaints.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return complaints.objects.all()