from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, UserAPIView, LogoutAPIView, ProfileAPIView, ProfilePasswordAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('users/info', ProfileAPIView.as_view()),
    path('users/password', ProfilePasswordAPIView.as_view()),
]
