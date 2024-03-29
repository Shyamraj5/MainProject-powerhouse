from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from customer.views import *
router=DefaultRouter()
router.register("user",SignUpView,basename="userreg"),
router.register("cp",C_ProductModelViewset ,basename="userreg"),
router.register("cpurchace",CPurchaseViewSet,basename="cpurch"),
router.register("complaints",complaintView,basename="comp"),
router.register("service",servicesView,basename="ser"),
router.register('inventories', InventoryViewSet,basename='inv'),
router.register('itemRateing', itemRateingview,basename='itemrate'),
router.register('serviceRateing', serviceRateingview,basename='serrate'),
router.register('complaintRateing', complaintRateingview,basename='comprate'),
router.register('cart', Cartviewset,basename='cart'),
router.register('getorder', getorder,basename='getor'),
router.register('getallser', getallservice,basename='allservi'),
router.register('getallcomp', getallcomp,basename='allservi'),
router.register('adminresponce',AdminResponseViewSet,basename='admin'),
# router.register('cnt',AdminResponseViewSet/counts,basename='s'),
# router.register('notifications', NotificationViewSet, basename='unread-count')
# router.register('countnoti', NotificationViewSet,basename='admin'),




urlpatterns = [
     path('token',views.obtain_auth_token),
     # path('countnoti/', NotificationViewSet.as_view(), name='unread-count'),
   
    
    
]+router.urls