from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товара
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
]