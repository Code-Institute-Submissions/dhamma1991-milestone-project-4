# Generated by Django 2.0.13 on 2019-04-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevelSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_rank', models.IntegerField()),
                ('xp_threshold', models.IntegerField()),
            ],
        ),
    ]