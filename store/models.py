from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    category = models.ForeignKey(to="ProductCategory", on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity_available = models.FloatField()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

def generate_invoice_number():
    last_invoice = Sales.objects.all().order_by('id').last()
    if not last_invoice:
        return 'IN0001'
    invoice_no = last_invoice.invoice_number
    invoice_int = int(invoice_no.split('IN')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'IN' + str(new_invoice_int).zfill(4)
    return new_invoice_no


class Sales(models.Model):
    invoice_number = models.CharField(max_length=50, default=generate_invoice_number, blank=False)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField()
    vat_applied = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.invoice_number


class SalesProductDetails(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(to=Sales, on_delete=models.CASCADE, related_name='product_details')
    quantity = models.FloatField()

    def __str__(self):
        return self.product.name
