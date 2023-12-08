import os
from datetime import datetime
import requests
from django.db.models import Q
from django.shortcuts import get_object_or_404
from disptacher.settings import SEND_JWT_TOKEN

from .models import Client, Message, Dispatch

URL = 'https://probe.fbrq.cloud/v1/send/'


def send_messages(data):
    client_filters = [
        filter.strip() for filter in data.get('client_filter').split(',')
    ]
    clients = Client.objects.filter(
        Q(operator__in=client_filters) | Q(tag__in=client_filters)
    )
    dispatch_id = data.get('id')
    dispatch = get_object_or_404(Dispatch, id=dispatch_id)
    for client in clients:
        message = Message.objects.create(
            client_id=client,
            send_date=datetime.now(),
            dispatch_status=False,
            dispatch=dispatch
        )
        url = f'{URL}0'
        payload = {
            'phone': client.phone,
            'text': data.get('text')
        }
        headers = {
            'Authorization': f'Bearer {SEND_JWT_TOKEN}',
        }
        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers
            )
            if response.status_code == 200:
                message.dispatch_status = True
                message.save()
                print(f'Сообщение успешно отправлено для: {client.phone}')
            else:
                print(
                    f'Не доставлено: {client.phone}, {response.status_code}'
                )
        except Exception as e:
            print(e)
