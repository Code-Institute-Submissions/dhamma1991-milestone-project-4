# Generated by Django 2.0.13 on 2019-04-18 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190418_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='level_rank',
        ),
    ]
