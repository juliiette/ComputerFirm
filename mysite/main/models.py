from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


class Positions(models.Model):
    position_id = models.AutoField('Position ID', primary_key=True)
    name = models.CharField('Position name', max_length=50)
    salary = models.PositiveIntegerField('Salary')
    duties = models.TextField('Duties', null=True, blank=True)
    demands = models.TextField('Demands', null=True, blank=True)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name


class Employees(models.Model):
    employee_id = models.AutoField('Employee ID', primary_key=True)
    first_name = models.CharField('First Name', max_length=50)
    second_name = models.CharField('Last Name', max_length=50)
    birthday = models.DateField('Birthday date', null=True, blank=True)
    sex = models.CharField('Gender', max_length=20, null=True, blank=True)
    address = models.CharField('Address', max_length=100, null=True, blank=True)
    phone = models.CharField('Phone number', max_length=15, null=True, blank=True)
    passport = models.CharField('Passport code', max_length=15, null=True, blank=True)
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE, verbose_name='Related position', null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def formatted_phone(self, country=None):
        return phonenumbers.parse(self.phone, country)

    def get_absolute_url(self):
        return f'/employees_home/{self.employee_id}'


class Customers(models.Model):
    customer_id = models.AutoField('Customer ID', primary_key=True)
    first_name = models.CharField('First Name', max_length=50)
    second_name = models.CharField('Last Name', max_length=50)
    address = models.CharField('Address', max_length=100, null=True, blank=True)
    phone = models.CharField('Phone number', max_length=15)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'



