from django.urls import path, include
from rest_framework import routers
from store.views import ProductViewSet, ProductCategoryViewSet

app_name = 'store'

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product-category', ProductCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
