from django.urls import path, include


urlpatterns = [
    path('products/', include('products.products_urls'), name='product-list'),
    path('categories/', include('products.categories_urls'), name='categories')
]


