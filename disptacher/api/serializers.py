from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import Client, Dispatch, Message


class DispatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dispatch
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'(7)+\d{10}$',
                message='Номер должен быть в формате: 7XXXXXXXXXX',
            )
        ]
    )
    operator = serializers.CharField(
        max_length=3,
        allow_blank=True,
        validators=[
            RegexValidator(
                regex=r'^\d{3}$',
                message=('Оператор должен быть в формате: \
                         123 или пустым полем для автозаполнения'),
            )
        ]
    )

    def validate(self, data):
        phone = data.get('phone', None)

        if phone:
            operator = phone[1:4]
            data['operator'] = operator

        return data

    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
