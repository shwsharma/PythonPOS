from rest_framework import serializers
from store.models import ProductCategory, Product, SalesProductDetails, Sales


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class SalesProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesProductDetails
        fields = '__all__'
        read_only_fields = ['sale']


class SalesSerializer(serializers.ModelSerializer):
    product_details = SalesProductDetailsSerializer(many=True)

    class Meta:
        model = Sales
        fields = ['id', 'invoice_number', 'employee', 'created', 'product_details', 'discount', 'vat_applied', 'total']
        read_only_fields = ['invoice_number', 'employee', 'created']

    def create(self, validated_data):
        product_details = validated_data.pop('product_details')
        sale = Sales.objects.create(employee=self.context.get("request").user, **validated_data)
        for product_detail in product_details:
            SalesProductDetails.objects.create(sale=sale, **product_detail)
        return sale

    def update(self, instance, validated_data):
        product_details = validated_data.pop('product_details')
        product_details_instance = instance.product_details

        instance.discount = validated_data.get('discount', instance.discount)
        instance.vat_applied = validated_data.get('vat_applied', instance.vat_applied)
        instance.total = validated_data.get('total', instance.total)
        instance.save()

        product_details_instance.is_premium_member = product_details.get(
            'product',
            product_details.is_premium_member
        )
        product_details_instance.has_support_contract = product_details.get(
            'quantity',
            product_details.has_support_contract
        )
        product_details_instance.save()

        return instance
