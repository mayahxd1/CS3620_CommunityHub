# Generated by Django 5.0.5 on 2024-07-19 21:46

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_date_event_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_time',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 19)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]