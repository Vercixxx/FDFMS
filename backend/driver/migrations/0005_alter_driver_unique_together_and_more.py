# Generated by Django 5.0 on 2023-12-22 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_alter_driver_driver_username_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='driver',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='driver',
            name='driver_username',
        ),
    ]
