# Generated by Django 4.2.4 on 2023-10-19 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vin', models.TextField(max_length=17)),
                ('brand', models.TextField()),
                ('model', models.TextField()),
                ('year_of_prod', models.PositiveIntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023)),
                ('color', models.TextField()),
                ('mileage', models.IntegerField(default=0)),
                ('engine_cap', models.FloatField()),
                ('engine_pow', models.IntegerField()),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=20)),
                ('policy_number', models.TextField()),
                ('is_oc', models.BooleanField()),
                ('is_ac', models.BooleanField()),
                ('phone_policy_contact', models.IntegerField()),
            ],
            options={
                'db_table': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='DriverCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('car_mileage', models.IntegerField(null=True)),
                ('car_condition', models.CharField(choices=[('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')], default='Good', max_length=20)),
                ('car_cleanliness', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default='5', max_length=5)),
                ('additional_remarks', models.TextField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
            options={
                'db_table': 'DD_report',
            },
        ),
    ]
