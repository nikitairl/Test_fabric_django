from django.db import models
import pytz

TIMEZONE_CHOICES = zip(pytz.common_timezones, pytz.common_timezones)


class Dispatch(models.Model):
    id = models.AutoField(primary_key=True)
    dispatch_date = models.DateTimeField()
    text = models.TextField()
    client_filter = models.TextField()
    dispatch_date_end = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Dispatch id: {self.id}'


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12)
    operator = models.CharField(max_length=3)
    tag = models.CharField(max_length=30)
    timezone = models.CharField(
        max_length=255,
        default='UTC',
        choices=TIMEZONE_CHOICES
    )

    def __str__(self):
        return f'Client id: {self.id}'


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    send_date = models.DateTimeField()
    dispatch_status = models.BooleanField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE)

    def __str__(self):
        return f'Message id: {self.id}'
