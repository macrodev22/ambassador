from rest_framework import serializers

from core.models import Link,Product,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Link
        fields = '__all__'