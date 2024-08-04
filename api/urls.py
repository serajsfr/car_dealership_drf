from django.urls import path, include
from .views import CarViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]