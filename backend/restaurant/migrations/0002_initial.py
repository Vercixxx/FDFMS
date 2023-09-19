# Generated by Django 4.2.4 on 2023-09-17 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('rest_manager', '0001_initial'),
        ('driver', '0002_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workchange',
            name='driver',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.driver'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='daily_cars_schedules',
            field=models.ManyToManyField(blank=True, to='restaurant.dailycarschedule'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='managers',
            field=models.ManyToManyField(blank=True, to='rest_manager.restmanager'),
        ),
        migrations.AddField(
            model_name='dailycarschedule',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car'),
        ),
        migrations.AddField(
            model_name='dailycarschedule',
            name='work_changes',
            field=models.ManyToManyField(blank=True, to='restaurant.workchange'),
        ),
    ]
