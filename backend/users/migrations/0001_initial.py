# Generated by Django 4.2.4 on 2023-10-19 13:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_role', models.CharField(choices=[('Owner', 'Owner'), ('HR', 'HR'), ('Payroll', 'Payroll'), ('Asset', 'Asset'), ('Clients', 'Clients'), ('Manager', 'Manager'), ('Driver', 'Driver'), ('Administrator', 'Administrator')], default='Administrator', max_length=20)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('residence_country', models.CharField(blank=True, max_length=100, null=True)),
                ('residence_city', models.CharField(blank=True, max_length=100, null=True)),
                ('residence_state', models.CharField(blank=True, max_length=100, null=True)),
                ('residence_street', models.CharField(blank=True, max_length=200, null=True)),
                ('residence_home_number', models.CharField(blank=True, max_length=10, null=True)),
                ('residence_apartament_number', models.CharField(blank=True, max_length=10, null=True)),
                ('residence_zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('registered_country', models.CharField(blank=True, max_length=100, null=True)),
                ('registered_city', models.CharField(blank=True, max_length=100, null=True)),
                ('registered_state', models.CharField(blank=True, max_length=100, null=True)),
                ('registered_street', models.CharField(blank=True, max_length=200, null=True)),
                ('registered_home_number', models.CharField(blank=True, max_length=10, null=True)),
                ('registered_apartament_number', models.CharField(blank=True, max_length=10, null=True)),
                ('registered_zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('correspondence_country', models.CharField(blank=True, max_length=100, null=True)),
                ('correspondence_city', models.CharField(blank=True, max_length=100, null=True)),
                ('correspondence_state', models.CharField(blank=True, max_length=100, null=True)),
                ('correspondence_street', models.CharField(blank=True, max_length=200, null=True)),
                ('correspondence_home_number', models.CharField(blank=True, max_length=10, null=True)),
                ('correspondence_apartament_number', models.CharField(blank=True, max_length=10, null=True)),
                ('correspondence_zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=30, null=True)),
                ('pesel_nip', models.CharField(blank=True, max_length=12, null=True)),
                ('tax_office_name', models.CharField(blank=True, max_length=80, null=True)),
                ('tax_office_address', models.CharField(blank=True, max_length=220, null=True)),
                ('nfz', models.CharField(blank=True, max_length=200, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
