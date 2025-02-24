from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Category, Review 
from products.serializers import ProductSerializer, CategorySerializers, ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from products.filters import ProductFilterSet
from rest_framework.filters import SearchFilter, OrderingFilter
from products.pagination import CustomPagination

class ProductViewList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilterSet
    pagination_class = CustomPagination  
    search_fields = ['name','description', 'category__name']
    ordering_fields = ['price', 'stock']

    
class CategoryViewList(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers


class ReviewViewList(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}  