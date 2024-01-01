# Generated by Django 5.0 on 2023-12-22 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0002_initial'),
        ('rest_manager', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='managers',
            field=models.ManyToManyField(blank=True, to='rest_manager.restmanager'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='daily_cars_schedules',
            field=models.ManyToManyField(blank=True, to='restaurant.dailycarschedule'),
        ),
        migrations.AddField(
            model_name='workchange',
            name='driver',
            field=models.ForeignKey(db_column='driver', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.driver'),
        ),
        migrations.AddField(
            model_name='dailycarschedule',
            name='work_changes',
            field=models.ManyToManyField(blank=True, to='restaurant.workchange'),
        ),
    ]
