from django.urls import path,include

from .views import LinksAPIView,OrdersAPIView

urlpatterns = [
    path('links/<str:code>', LinksAPIView.as_view()),
    path('orders', OrdersAPIView.as_view()),
]