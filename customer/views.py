from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.views import APIView
from .models import  *
from .serializers import *
from rest_framework.response import Response
from rest_framework import permissions,authentication,status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework import status
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
    
 
    def destroy(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            C_Orders.objects.filter(id=id).delete()
            return Response({"msg":"Deleted"})

class getorder(ModelViewSet):
    queryset = C_Orders.objects.all()
    serializer_class = getorderser
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        return C_Orders.objects.filter(user=self.request.user)
    

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
    

    
  
    
    def create(self,request,*args,**kwargs):
        
        id=request.data.get('product')
       
        print(id)
        cp=CustomerProduct.objects.get(id=id)
        Cart.objects.create(product=cp,user=self.request.user)
        return Response({"msg":"addes to cart"})
    


    def destroy(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            Cart.objects.filter(id=id).delete()
            return Response({"msg":"Deleted"})


    
   


class AdminResponseViewSet(ModelViewSet):
    queryset = AdminResponse.objects.all()
    serializer_class = AdminResponseSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    ser=serviceser()

    def create(self,request):
        id=request.data.get('service')
        
        print(id)
        service=services.objects.get(id=id)
        service_id=service.id
        response=request.data.get('response')
        
        ser=AdminResponseSerializer(data={"service":service_id,"response":response})
        if ser.is_valid():
            ser.save()
            return Response({"msg":"ok"})
        return Response(data=ser.errors)
    
     
     
    def get_queryset(self):
        user = self.request.user  
        return AdminResponse.objects.filter(service__user=user)
    

    def destroy(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            AdminResponse.objects.filter(id=id).delete()
            return Response({"msg":"Deleted"})

    @action(detail=False, methods=['GET'])      
    def counts(self, request):
        user = self.request.user  # Assuming you're using Django's built-in User model
        unread_count = AdminResponse.objects.filter(is_read=False,service__user=user).count()
        print(unread_count)
        return Response({unread_count})


