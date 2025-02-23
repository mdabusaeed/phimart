from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializers
from django.db.models import Count

@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_products(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=204)


@api_view(['GET','POST'])
def view_catogories(request):
    if request.method == 'GET':
        category = Category.objects.annotate(product_count = Count('products')).all()
        serializer = CategorySerializers(category, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializers(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view()
def view_specifiq_category(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializers(category)
    return Response(serializer.data)
