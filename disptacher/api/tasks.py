from disptacher.celery import app
from celery import shared_task
from .service import send_messages
from .models import Dispatch


@shared_task
def send_messages_task(data):
    try:
        send_messages(data)
    except Exception as e:
        print(e)


def schedule_send_messages(data):
    dispatch_date = data.get('dispatch_date')
    send_messages_task.apply_async(args=[data], eta=dispatch_date)
