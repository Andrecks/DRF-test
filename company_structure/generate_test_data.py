import random
from django.contrib.auth.models import User
from employees.models import Employee, Department

# create some test users
for i in range(10):
    username = f'user{i}'
    password = 'password'
    email = f'user{i}@example.com'
    User.objects.create_user(username=username, password=password, email=email)

# create some test departments
department_names = ['Sales', 'Marketing', 'Engineering', 'Operations']
for name in department_names:
    department = Department.objects.create(name=name)

    # create a director for each department
    username = f'{name.lower()}_director'
    password = 'password'
    email = f'{name.lower()}_director@example.com'
    user = User.objects.create_user(username=username, password=password, email=email)
    director = Employee.objects.create(user=user, name=f'{name} Director')
    department.director = director
    department.save()

# create some test employees
for i in range(100):
    name = f'Employee {i}'
    salary = random.randint(30000, 100000)
    hire_date = '2022-03-29'
    department = random.choice(Department.objects.all())
    Employee.objects.create(name=name, salary=salary, hire_date=hire_date, department=department)
