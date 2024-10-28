from django.shortcuts import render
from rest_framework.views import APIView,Response
from rest_framework import exceptions,status
import stripe
from django.db import transaction
import stripe.error

from core.models import Link, Order, OrderItem, Product
from .serializers import LinkSerializer
# Create your views here.

class LinksAPIView(APIView):
    def get(self, request, code):
        link = Link.objects.filter(code=code).first()

        serializer = LinkSerializer(link)
        return Response(serializer.data)

class OrdersAPIView(APIView):

    @transaction.atomic
    def post(self, request):
        data = request.data
        link = Link.objects.filter(code=data['code']).first()

        if not link:
            raise exceptions.NotFound('Link not found')
        
        order = self.create_order(link, data)

        line_items = self.create_order_items(order,products=data.get('products', []))
            
        BASE_URL = request.build_absolute_uri('/')
        query_params = '?source={CHECKOUT_SESSION_ID}'

        stripe.api_key = 'sk_test_51NWJ1oFHLENO3a2Y5tWRZRyvDFWEOLQvSg8VCAmgdwhysjRp33C99hWnhuCD6MhaeQEcbROzNaqS0U4EkNv3bdj300BIUPLidM'
        
        #Create stripe session
        transaction.on_commit(lambda: self.create_stripe_checkout_session(order,BASE_URL, query_params, line_items))
        return Response({
            'message': 'Order created successfully, payment pending',
        }, status=status.HTTP_201_CREATED)


    def create_order(self, link, data):
        order = Order()
        order.code = link.code
        order.user = link.user
        order.ambassador_email = link.user.email
        order.first_name = data.get('first_name', None)
        order.last_name = data.get('last_name', None)
        order.email = data.get('email')
        order.address = data.get('address', None)
        order.country = data.get('country')
        order.city = data.get('city')
        order.zip = data.get('zip')
        order.save()
        return order
    
    def create_order_items(self, order, products):
        line_items = []
        for item in products:
            product = Product.objects.get(pk=item.get('product_id'))
            quatity = item.get('quantity')

            # Create order item
            order_item = OrderItem()
            order_item.order = order
            order_item.product_tile = product.title
            order_item.price = product.price
            order_item.quantity = quatity

            order_item.save()
            
            line_items.append({
                'name': product.title,
                'description': product.description,
                'images': [product.image],
                'amount' : int(product.price * 100),
                'currency' : 'ugx',
                'quantity' : quatity
            })

            return line_items
        
    def create_stripe_checkout_session(self,order, BASE_URL, query_params, line_items):
        try:
            stripe_line_items = [
            {
                'price_data': {
                    'currency': 'ugx',
                    'product_data': {
                        'name': item['name'],
                        'description': item['description'],
                        'images': item['images'],
                    },
                    'unit_amount': item['amount'],  # amount should be in cents
                },
                'quantity': item['quantity'],
            }
            for item in line_items
            ]
            source = stripe.checkout.Session.create(
            success_url=f"{BASE_URL}success{query_params}",
            cancel_url= f"{BASE_URL}error",
            payment_method_types= ['card'],
            line_items=stripe_line_items,
            mode='payment',
            )

            order.transaction_id = source.id
            order.save()
        except stripe.error.StripeError as e:
            raise exceptions.APIException('Stripe error: ' + str(e))
   