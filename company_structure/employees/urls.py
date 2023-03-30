from django.urls import path
from .views import employee_list, create_employee, delete_employee, department_list

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('create_employee/', create_employee, name='create_employee'),
    path('delete_employee/', delete_employee, name='delete_employee'),
    path('department_list/', department_list, name='department_list'),
]