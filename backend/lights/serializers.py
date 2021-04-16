from rest_framework import serializers

from lights.models import Light

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ('id','name','state')