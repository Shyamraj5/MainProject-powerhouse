
from django.urls import path
from .views import *
from rest_framework.authtoken import views
from owner.models import *
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
# routers.register("cpurchace",CPurchaseViewSet,basename="cpurch"),


urlpatterns=[
    path('token',views.obtain_auth_token)
]+routers.urls