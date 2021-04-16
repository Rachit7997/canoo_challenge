from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from thermostat.models import Temperature
from thermostat.serializers import TemperatureSerializer

class TemperatureList(ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureCreate(CreateAPIView):
    serializer_class = TemperatureSerializer

class TemperatureRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    lookup_field = 'id'