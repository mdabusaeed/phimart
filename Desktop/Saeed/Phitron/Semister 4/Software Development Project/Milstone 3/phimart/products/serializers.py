from rest_framework import serializers
from decimal import Decimal
from products.models import Category, Product, Review

class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField() 
    class Meta:
        model = Category
        fields = ['id','name','description','product_count']
        read_only_fields = ["product_count"]

    def get_product_count(self, obj):
        return Product.objects.filter(category=obj).count()
 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'category','price', 'price_with_tax']


    price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    def calculate_tax(self,product):
        return round(product.price * Decimal(1.1), 2)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        product = Product.objects.get(pk=product_id)
        review = Review.objects.create(product=product, **validated_data)
        return review 
