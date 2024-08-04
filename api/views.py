from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import CarSerializer
from .models import Car


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cars to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]