from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.response import Response
from django.core.cache import cache

from administrator.serializers import LinkSerializer, OrderSerializer, ProductSerializer
from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from core.models import Link, Order, Product, User


# Create your views here.

def clear_cache():
    cache.delete('products_backend')
    for key in cache.keys('*'):
        if 'products_frontend' in key:
            cache.delete(key)

class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        results = User.objects.filter(is_ambassador=True)

        serializer = UserSerializer(results, many=True)
        return Response(serializer.data)
    

class ProductGenericAPIView(
    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    ):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None):
        if pk is not None:
            return self.retrieve(request, pk)
        return self.list(request)
    
    def post(self, request):
        response = self.create(request)
        clear_cache()
        return response
    
    def put(self, request, pk=None):
        response = self.partial_update(request, pk)
        clear_cache()
        return response

    def delete(self, request, pk=None):
        response = self.destroy(request, pk)
        clear_cache()
        return response
    
class LinksAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Get the user
        user = User.objects.get(pk=pk)
        links = Link.objects.filter(user=user)

        serializer = LinkSerializer(links,many=True)
        return Response(serializer.data)
    
class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Return completed orders
        orders = Order.objects.filter(complete=True)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)