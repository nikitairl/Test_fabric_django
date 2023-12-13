import logging
from datetime import datetime, timedelta, timezone

import pytz
import requests
from celery import shared_task
from django.db.models import Q
from django.shortcuts import get_object_or_404

from disptacher.settings import SEND_JWT_TOKEN

from .models import Client, Dispatch, Message

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
        client_timezone = pytz.timezone(client.timezone)
        current_timezone = datetime.now().replace(tzinfo=timezone.utc)
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
        headers = {
            'Authorization': f'Bearer {SEND_JWT_TOKEN}',
        }
        dispatch_date = datetime.fromisoformat(str(dispatch_date))
        eta = dispatch_date.astimezone(client_timezone)
        end_date = datetime.fromisoformat(str(dispatch_date_end))
        expires = end_date.astimezone(client_timezone)
        try:
            if eta < current_timezone:
                expires = expires + timedelta(days=1)
                eta = eta + timedelta(days=1)
        except Exception as e:
            raise Exception(f'{eta}, {datetime.now()}, {e}')
        send_message_task.apply_async(
            args=[message.id, payload, headers, expires],
            eta=eta,
            expires=expires
        )


@shared_task(bind=True, max_retries=5, default_retry_delay=30)
def send_message_task(self, message_id, payload, headers, end_date):
    now = datetime.now(timezone.utc)
    if now < end_date:
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
    else:
        logging.error('Время вышло')
