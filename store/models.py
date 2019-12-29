from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    category = models.ForeignKey(to="ProductCategory", on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
