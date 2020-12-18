from django.shortcuts import render, redirect
from .models import *
from .forms import EmployeesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    data = {'title': 'Main Page'
    }
    return render(request, 'main/index.html', data)


def add_employee(request):
    error = ''
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_home')
        else:
            error = 'Wrong form'

    form = EmployeesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_employee.html', data)


def employees_home(request):
    employees = Employees.objects.all()
    return render(request, 'main/employees_home.html', {'employees': employees})


class EmployeesDetailView(DetailView):
    model = Employees
    template_name = 'main/details_view.html'
    context_object_name = 'employee'


class EmployeesUpdateView(UpdateView):
    model = Employees
    template_name = 'main/add_employee.html'

    # fields = ['first_name', 'second_name', 'birthday', 'sex', 'address', 'phone', 'passport', 'position_id']
    form_class = EmployeesForm


class EmployeesDeleteView(DeleteView):
    model = Employees
    template_name = 'main/delete_employee.html'
    success_url = '/main/employees_home.html'


def positions_home(request):
    positions = Positions.objects.all()
    return render(request, 'main/positions.html', {'positions': positions})


def customers_home(request):
    customers = Customers.objects.all()
    return render(request, 'main/customers.html', {'customers': customers})


