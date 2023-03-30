from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_list(request):
    employees = Employee.objects.all()

    # Filter by department id if present in request
    department_id = request.GET.get('department_id')
    if department_id:
        employees = employees.filter(department__id=department_id)

    # Check if there is a search query for surname in the request
    surname = request.GET.get('surname', '')
    if surname:
        employees = employees.filter(surname__icontains=surname)

    # Paginate the results
    paginator = Paginator(employees, 10) # Show 10 employees per page
    page = request.GET.get('page')

    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    serializer = EmployeeSerializer(employees, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return Response(status=204)
    except Employee.DoesNotExist:
        return Response(status=404)


@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)