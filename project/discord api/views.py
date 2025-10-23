# views.py
from django.http import JsonResponse
from models import Employee
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@login_required # Ensures that only authenticated users can access this view #
def dashboard(request):
    return HttpResponse("Welcome to your dashboard!")

def employee_list(request):
    employees = Employee.objects.all().values('name', 'age', 'department')
    return JsonResponse(list(employees), safe=False)

