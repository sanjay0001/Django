from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from main.models import *
from rest_framework.views import APIView
# from rest_framework.generics import 
from rest_framework.generics import ListAPIView


class CustomListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data={"data":response.data,"list":"object"}
        return response


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


class Display(APIView):
  
    def get(self,*request):
        print(request[1])
        if len(request)==1:
            return Response("Hello")
        
        obj=Product.objects.get(pk=id)
        s=ProductSerializer(obj)
        return Response(s.data)
    