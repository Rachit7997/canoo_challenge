from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from thermostat.models import Temperature
from thermostat.serializers import TemperatureSerializer

class TemperatureList(ListAPIView):
#Responses with the list of Temperatures as JSON
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureCreate(CreateAPIView):
#Create new temperature and responses with newly created temperature 
    serializer_class = TemperatureSerializer

class TemperatureRetrieveUpdate(RetrieveUpdateAPIView):
    """
    Responses with the temperature value as JSON
    Update the value of temperature and responses with the updated temperature as JSON
    """
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    lookup_field = 'id'