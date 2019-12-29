from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from store.models import ProductCategory, Product
from store.serializers import ProductCategorySerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    authentication_classes = [BasicAuthentication]
