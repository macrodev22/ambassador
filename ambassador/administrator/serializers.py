from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from core.models import Link, Order, OrderItem, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link 
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem 
        fields = '__all__'

class OrderSerializer(ModelSerializer):

    order_items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        items = OrderItem.objects.filter(order_id=obj.id)
        return sum((o.price * o.quantity) for o in items)

    class Meta:
        model = Order 
        fields = '__all__'