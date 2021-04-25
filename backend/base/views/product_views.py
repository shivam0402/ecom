from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import  status
from ..models import Product
from ..products import products
from ..serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password



@api_view(['GET', 'POST'])
def getProducts(request):
    Products = Product.objects.all()
    serializer = ProductSerializer(Products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getProduct(request, pk):
    product = ProductSerializer(Product.objects.get(_id=pk), many=False)
    return Response(product.data)
