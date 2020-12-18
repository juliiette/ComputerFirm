from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('employees_home', views.employees_home, name='employees_home'),
    path('positions_home', views.positions_home, name='positions_home'),
    path('customers_home', views.customers_home, name='customers_home'),
    path('employees_home/<int:pk>', views.EmployeesDetailView.as_view(), name='employee-detail'),
    path('employees_home/<int:pk>/update', views.EmployeesUpdateView.as_view(), name='employee-update'),
    path('employees_home/<int:pk>/delete', views.EmployeesDeleteView.as_view(), name='employee-delete')

]