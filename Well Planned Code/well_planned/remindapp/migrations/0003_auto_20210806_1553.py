# Generated by Django 3.1.4 on 2021-08-06 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remindapp', '0002_auto_20210806_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='current_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 15, 53, 4, 677889)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='reminder_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 15, 53, 4, 677889)),
        ),
    ]