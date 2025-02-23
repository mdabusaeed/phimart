from django.urls import path
from products import views

urlpatterns = [
    path('', views.view_catogories, name='category-list'),
    path('<int:id>/', views.view_specifiq_category, name='view_specifiq_category')
]
