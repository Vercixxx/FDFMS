# Generated by Django 5.0.1 on 2024-02-10 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0007_wagetariff_driver_wage_tariff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='wage_tariff',
            field=models.ForeignKey(blank=True, db_column='wage_tariff', null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.wagetariff'),
        ),
    ]
