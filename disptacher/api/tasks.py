import logging
from datetime import datetime

import requests
from celery import shared_task
from django.db.models import Q
from django.shortcuts import get_object_or_404

from disptacher.settings import SEND_JWT_TOKEN

from .models import Client, Dispatch, Message
from .utils import delta_calc

URL = 'https://probe.fbrq.cloud/v1/send/'


def schedule_send_message(data):

    dispatch_date = data.get('dispatch_date')
    dispatch_date_end = data.get('dispatch_date_end')
    dispatch = get_object_or_404(Dispatch, id=data.get('id'))
    client_filters = [
        filter.strip() for filter in data.get('client_filter').split(',')
    ]
    clients = Client.objects.filter(
        Q(operator__in=client_filters) | Q(tag__in=client_filters)
    )
    print(clients.count())
    for client in clients:
        message = Message.objects.create(
            client_id=client,
            send_date=dispatch_date,
            dispatch_status=False,
            dispatch=dispatch
        )
        payload = {
            'phone': client.phone,
            'text': data.get('text')
        }
        dispatch_date = delta_calc(dispatch_date, client.timezone)
        dispatch_date_end = delta_calc(dispatch_date_end, client.timezone)
        send_message_task.apply_async(
            args=[message.id, payload, client.timezone],
            eta=dispatch_date,
            expires=dispatch_date_end,
        )


@shared_task(bind=True, max_retries=5, default_retry_delay=30)
def send_message_task(self, message_id, payload, timezone):
    headers = {
        'Authorization': f'Bearer {SEND_JWT_TOKEN}',
    }
    response = requests.post(
        URL + '0',
        json=payload,
        headers=headers
    )
    if response.status_code == 200:
        message = get_object_or_404(Message, id=message_id)
        message.dispatch_status = True
        message.send_date = datetime.now()
        message.save()
        print(f'Сообщение успешно отправлено для: {payload["phone"]}')
    else:
        logging.error(response.status_code)
        self.retry()
