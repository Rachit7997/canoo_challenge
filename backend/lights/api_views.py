from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from lights.models import Light
from lights.serializers import LightSerializer

class LightList(ListAPIView):
# Responses with the list of Lights 
    queryset = Light.objects.all()
    serializer_class = LightSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

class LightCreate(CreateAPIView): 
# Creates Light and Responses with JSON of newly created Light
    serializer_class = LightSerializer


class LightRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Resposnes with JSON of a queried light
    Update the Light and send the updated Light as JSON
    Delete the Light and send the deleted Light as JSON
    """ 
    queryset = Light.objects.all()                               
    serializer_class = LightSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        Light_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete(f"light_data_{Light_id}")
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            light = response.data
            cache.set(f"light_data_{light['id']}", {
                'name':light['name'],
                'state':light['state']
            })
        return response
