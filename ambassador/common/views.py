from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .authentication import JWTAuthentication
from core.models import User

from .serializers import UserSerializer

# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match')
        
        data['is_ambassador'] = 'api/ambassador' in request.path

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        email =data.get('email', None)
        password = data.get('password', None)

        scope = 'ambassador' if 'api/ambassador' in request.path else 'admin'

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Incorrect password") 

        #Generate a JWT
        token = JWTAuthentication.generate_jwt(user.id, scope)
        
        response_data = UserSerializer(user).data
        response_data['jwt'] = token

        #Send JWT as HTTP cookie
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        # response.set_cookie(key='samesite', value=None)
        response.data = response_data

        return response   

# Return a single loged in user
class UserAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = UserSerializer(user).data

        # Add revenue if on ambassador route
        if 'api/ambassador' in request.path:
            data['revenue'] = user.revenue

        return Response(data)

class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'status': 'success'
        }
        return response
    
class ProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data
        passwords = {
            'password': data.get('password', None),
            'password_confirm': data.get('password_confirm', None)
        }
        if None in passwords.values():
            raise exceptions.APIException('Password and password confirm are mandatory')
        
        if passwords['password'] != passwords['password_confirm']:
            raise exceptions.APIException('Passwords do not match')
        
        user.set_password(passwords['password'])
        user.save()
        return Response(UserSerializer(user).data)