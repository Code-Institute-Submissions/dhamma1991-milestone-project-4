# Generated by Django 2.0.13 on 2019-04-11 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20190411_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 16, 52, 21, 642120, tzinfo=utc), editable=False),
        ),
    ]
