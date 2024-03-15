from rest_framework import viewsets
from .models import Employee, Department, Position
from .serializers import EmployeeSerializer, DepartmentSerializer, PositionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from django.contrib.auth.hashers import check_password

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

from django.http import JsonResponse
from .models import Employee

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            employee = Employee.objects.get(email=email)
            if employee.password == password:
                # Aquí podrías hacer otras comprobaciones de autenticación si es necesario
                return JsonResponse({'message': 'Inicio de sesión exitoso'})
            else:
                return JsonResponse({'error': 'Contraseña incorrecta'}, status=401)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)



