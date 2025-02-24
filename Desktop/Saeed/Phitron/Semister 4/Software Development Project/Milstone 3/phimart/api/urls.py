from django.urls import path, include
from products.views import ProductViewList, CategoryViewList, ReviewViewList
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewList, basename='products')
router.register('categories', CategoryViewList)

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewList, basename='product-reviews')
 


urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
]


