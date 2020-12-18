# Generated by Django 3.2 on 2020-11-27 15:03

from django.db import migrations, models
import django.db.models.deletion
from phonenumber_field.modelfields import PhoneNumberField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Customer ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('phone', models.CharField(verbose_name='Phone number', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Position ID')),
                ('name', models.CharField(max_length=50, verbose_name='Position name')),
                ('salary', models.PositiveIntegerField(max_length=10, verbose_name='Salary')),
                ('duties', models.TextField(verbose_name='Duties')),
                ('demands', models.TextField(verbose_name='Demands')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('birthday', models.DateField(verbose_name='Birthday date')),
                ('sex', models.CharField(max_length=20, verbose_name='Gender')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('phone', models.CharField(verbose_name='Phone number', max_length=15)),
                ('passport', models.CharField(max_length=15, verbose_name='Passport code')),
                ('position_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.positions', verbose_name='Related position')),
            ],
        ),
    ]
