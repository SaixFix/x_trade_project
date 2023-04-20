from rest_framework import serializers

from trade_net.models.base import Address, Product
from trade_net.models.factory import Factory
from trade_net.serializers.base import AddressPartSerializer, ProductPartSerializer


class FactoryCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    debt = serializers.DecimalField(required=False)
    address = AddressPartSerializer(
        read_only=True,
        many=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ("id", "created")

    def is_valid(self, *, raise_exception=False):
        """отлючаем выпадение ошибки в случае если принятова адреcа или не существует"""
        self._address = self.initial_data.pop('address')
        self._product = self.initial_data.pop('product')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        """переопределили метод create для возможности получит или создать продукт и адресс"""
        factory = Factory.objects.create(**validated_data)
        address, _ = Address.objects.get_or_create(**self._address)
        product, _ = Product.objects.get_or_create(**self._product)
        factory.address.add(address)
        factory.product.add(product)

        return factory


class FactoryListSerializer(serializers.ModelSerializer):
    address = AddressPartSerializer(
        read_only=True,
        many=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = '__all__'
