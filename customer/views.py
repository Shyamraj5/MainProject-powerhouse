from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import  *
from .serializers import *
from rest_framework.response import Response
from rest_framework import permissions,authentication,status
from rest_framework.decorators import action
# Create your views here.
class CPurchaseViewSet(ModelViewSet):
    queryset = C_Orders.objects.all()
    serializer_class = CustSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request):
        ser=CustSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    def get_queryset(self):
        return CustomerProduct.objects.filter(user=self.request.user)

class complaintView(ModelViewSet):
    serializer_class=complaintser
    queryset=complaints.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser=complaintser(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    def get_queryset(self):
        return complaints.objects.filter(user=self.request.user)  
    


class servicesView(ModelViewSet):
    serializer_class=serviceser
    queryset=services.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser=serviceser(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    def get_queryset(self):
        return services.objects.filter(user=self.request.user)
    

class itemRateingview(ModelViewSet):
    serializer_class=itemRating
    queryset=Itemrating.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser=itemRating(data=request.data)
        if ser.is_valid():
            ser.save(user=self.request.user)
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    

class serviceRateingview(ModelViewSet):
    serializer_class=serviceRating
    queryset=Servicerating.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser=serviceRating(data=request.data)
        if ser.is_valid():
            ser.save(user=self.request.user)
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    

class complaintRateingview(ModelViewSet):
    serializer_class=complaintRating
    queryset=Complaintrating.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser=complaintRating(data=request.data)
        if ser.is_valid():
            ser.save(user=self.request.user)
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    
class Cartviewset(ModelViewSet):
    serializer_class=cartser
    queryset=Cart.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self,**kwargs):
 

        
        return Cart.objects.filter(user=self.request.user)

    # def create(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     Cart.objects.filter(id=id).create()
    #     return Response({"msg":"addes to cart"})
    @action(detail=True,methods=["post"])
    def add_cart(self,req,*args,**kwargs):
        id =kwargs.get("pk")
        cp=CustomerProduct.objects.get(id=id)
        user=req.user
        ser=cartser(data=req.data,context={"user":user,"cartP":cp})
        if ser.is_valid():
            ser.save()
            return Response ({"msg":"Added"})
        else:
            return Response({"MSG":ser.erros},status=status.HTTP_100_CONTINUE)