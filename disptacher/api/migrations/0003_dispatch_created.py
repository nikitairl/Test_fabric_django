# Generated by Django 5.0 on 2023-12-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_client_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatch',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
