# Generated by Django 2.0.13 on 2019-04-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190417_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_level',
            field=models.IntegerField(default=1),
        ),
    ]
