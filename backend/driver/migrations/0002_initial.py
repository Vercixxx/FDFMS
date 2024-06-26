# Generated by Django 5.0.1 on 2024-02-21 09:49

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('generaluser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('ln_release_date', models.DateField(blank=True, max_length=50, null=True)),
                ('ln_expire_date', models.DateField(blank=True, max_length=50, null=True)),
                ('ln_published_by', models.CharField(blank=True, max_length=70, null=True)),
                ('ln_code', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'Drivers',
            },
            bases=('users.generaluser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WageTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('basic_hourly_rate', models.FloatField()),
                ('orders_bonus', models.FloatField()),
                ('fuel_bonus', models.FloatField()),
                ('starting_new_billing_period', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'WageTariff',
            },
        ),
        migrations.AddField(
            model_name='dailywork',
            name='driver',
            field=models.ForeignKey(db_column='driver', on_delete=django.db.models.deletion.CASCADE, to='driver.driver'),
        ),
        migrations.AddField(
            model_name='driver',
            name='wage_tariff',
            field=models.ForeignKey(blank=True, db_column='wage_tariff', null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.wagetariff'),
        ),
    ]
