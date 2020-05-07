# Generated by Django 3.0.2 on 2020-05-07 04:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('babyteach', '0004_auto_20200507_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='summary',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='addtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 4, 15, 40, 236538, tzinfo=utc)),
        ),
    ]