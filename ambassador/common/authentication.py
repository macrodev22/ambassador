import jwt, datetime, time
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from ambassador import settings
from core.models import User


class JWTAuthentication(BaseAuthentication):

    @staticmethod
    def generate_jwt(userid, scope):

        payload = {
            'user_id': userid,
            'scope': scope,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat' : time.time()
        }

        return jwt.encode(payload, settings.SECRET_KEY, 'HS256')
    
    # Authenticate a user with JWT from Cookie
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('unauthenticated')

        user = User.objects.get(pk=payload['user_id'])

        # Check if JWT is still valid
        # TODO

        if user is None:
            raise exceptions.NotAuthenticated('user not found')
        
        # Check if user is ambassador or admin
        scope = payload['scope']
        route_user_type = 'ambassador' if('api/ambassador' in request.path) else 'admin'

        if scope != route_user_type:
            raise exceptions.NotAcceptable('not authorised invalid user type')

        return (user, token)
        