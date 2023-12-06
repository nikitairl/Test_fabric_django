from rest_framework import serializers
from .models import Dispatch


class DispatchSerializer(serializers.Serializer):

    class Meta:
        model = Dispatch
        fields = '__all__'
