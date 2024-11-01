import time, random, string
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated

from common.authentication import JWTAuthentication
from core.models import Link, Order, Product, User

from .serializers import LinkSerializer, ProductSerializer

# Create your views here.
class ProductFrontEndAPIView(APIView):
    @method_decorator(cache_page(60*60*2, key_prefix='products_frontend'))
    def get(self, request):
        products = Product.objects.all() 
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    

class ProductBackEndAPIView(APIView):

    def get(self, request):
        products = cache.get('products_backend')
        if not products:
            time.sleep(2) # improvisation
            products = list(Product.objects.all())
            cache.set('products_backend', products, timeout=60*30) # 30 minutes

        # Query params
        # Search
        s = request.query_params.get('s', '')
        if s:
            products = list([
                p for p in products
                if (s.lower() in p.title.lower()) or (s.lower() in p.description.lower())
            ])

        total = len(products)

        # Sort
        sort = request.query_params.get('sort', None)
        if sort:
            sort = sort.lower()
            if sort == 'asc':
                products.sort(key=lambda p: p.price)
            elif sort == 'desc':
                products.sort(key=lambda p: p.price, reverse=True)
        
        # paginate
        per_page=9
        page = request.query_params.get('page', 1)
        if not page:
            page=1
        page = int(page)
        start = (page - 1) * per_page
        end = page * per_page



        serializer = ProductSerializer(products[start:end], many=True)
        data = serializer.data

        return Response({
            'data': data,
            'meta' : {
                'page': page,
                'per_page': per_page,
                'total': total
            }
        })
    
class LinkAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        user = request.user

        data = {
            'user' : user.id,
            'code' : ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
            'products' : request.data.get('products', []),
        }

        serializer = LinkSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class StatsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user

        links = Link.objects.filter(user_id=user.id)
        

        return Response([(self.format(link=link)) for link in links])
    
    def format(self, link):
        orders = Order.objects.filter(code=link.code, complete=True)

        return {
            'code': link.code,
            'count' : len(orders),
            'revenue' : sum(o.ambassador_revenue for o in orders)
        }
    
class RankingsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        ambassadors = User.objects.filter(is_ambassador=True)

        response = list({
            'name': a.name,
            'revenue' : a.revenue
        } for a in ambassadors)
        response.sort(key=lambda a: a['revenue'], reverse=True)
        return Response(response)