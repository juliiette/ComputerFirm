# Generated by Django 3.2 on 2020-12-18 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='positions',
            options={'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.AlterField(
            model_name='customers',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday date'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='passport',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Passport code'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='position_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.positions', verbose_name='Related position'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='sex',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='positions',
            name='demands',
            field=models.TextField(blank=True, null=True, verbose_name='Demands'),
        ),
        migrations.AlterField(
            model_name='positions',
            name='duties',
            field=models.TextField(blank=True, null=True, verbose_name='Duties'),
        ),
        migrations.AlterField(
            model_name='positions',
            name='salary',
            field=models.PositiveIntegerField(verbose_name='Salary'),
        ),
    ]
