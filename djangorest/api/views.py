from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from main.models import *

@api_view(['GET'])
def show(request):
    product_s=ProductSerializer(Product.objects.all(),many=True)
    return Response(product_s.data)

@api_view(['POST'])
def add(request):
    s=ProductSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data)

@api_view(['GET'])
def get(request,id):
    id=request.id
    obj=Product.objects.get(id=id)
    s=ProductSerializer(obj)
    return Response(s.data)

