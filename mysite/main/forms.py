from .models import Employees
from django.forms import ModelForm, TextInput, DateTimeInput


class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = ['first_name', 'second_name', 'birthday', 'sex', 'address', 'phone', 'passport', 'position_id']

        widgets = {
            "first_name" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),


            "birthday": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of birth'
            }),
            "sex": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Gender'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            "passport": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Passport'
            }),
            "position_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Position'
            })
        }

