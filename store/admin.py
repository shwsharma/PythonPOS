from django.contrib import admin
from store.models import Product, ProductCategory, Sales, SalesProductDetails

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Sales)
admin.site.register(SalesProductDetails)
