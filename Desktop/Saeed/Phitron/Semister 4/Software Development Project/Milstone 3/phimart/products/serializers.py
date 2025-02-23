from rest_framework import serializers
from decimal import Decimal
from products.models import Category, Product

class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField() 
    class Meta:
        model = Category
        fields = ['id','name','description','product_count']
        read_only_fields = ["product_count"]

    def get_product_count(self, obj):
        return Product.objects.filter(category=obj).count()

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     tax = serializers.SerializerMethodField(method_name = 'calculate_tax_tax')
#     price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
#     # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     # category = serializers.StringRelatedField()
#     category = CategorySerializers()

#     def calculate_tax(self,product):
#         return round(product.price * Decimal(1.1), 2)
    
#     def calculate_tax_tax(self,product):
#         return round(self.calculate_tax(product) - product.price, 2)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'category','price', 'price_with_tax']


    price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    def calculate_tax(self,product):
        return round(product.price * Decimal(1.1), 2)