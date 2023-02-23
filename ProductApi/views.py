from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def list_all(request):
    product_data = Product.objects.all()
    serializer = ProductSerializer(product_data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

#gat single products by using product id 
@api_view(['GET'])
def view_product(request,pk):
    product_no = Product.objects.get(id=pk)
    serializer = ProductSerializer(product_no,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)

        
    

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Successfully Created",status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updated_product(request,pk):
    products_no = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products_no,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Successfully Updated The Product..",status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def delete_product(request,pk):
    product_no = Product.objects.get(id=pk)
    product_no.delete()
    return Response("Successfully Deleted..",status=status.HTTP_200_OK)

  
    
    
