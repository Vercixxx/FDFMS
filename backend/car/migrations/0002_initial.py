# Generated by Django 4.2.4 on 2023-09-17 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('driver', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivercar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.driver'),
        ),
    ]
