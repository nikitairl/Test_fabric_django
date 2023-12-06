# Generated by Django 5.0 on 2023-12-06 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=12)),
                ('operator', models.CharField(max_length=3)),
                ('tag', models.CharField(max_length=30)),
                ('timezone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dispatch_date', models.DateTimeField()),
                ('text', models.TextField()),
                ('client_filter', models.TextField()),
                ('dispatch_date_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_date', models.DateTimeField()),
                ('dispatch_status', models.BooleanField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
                ('dispatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dispatch')),
            ],
        ),
    ]
