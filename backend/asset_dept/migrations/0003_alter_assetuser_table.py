# Generated by Django 4.2.4 on 2023-09-15 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_dept', '0002_remove_assetuser_test_field'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='assetuser',
            table='AssetUser',
        ),
    ]
