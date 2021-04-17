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

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            Temp = response.data
            cache.set(f"light_data_{Temp['id']}",{
                'temp': Temp['temp']
            })