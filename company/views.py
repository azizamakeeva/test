from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from company.models import Employee, Department, ProgrammingLanguage
from company.serializer import EmployeeSerializers, DepartmentSerializers, ProgrammingLanguageSerializers


class EmployeeAPIViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'surname', 'age', 'sex', 'department', 'language']
    ordering_fields = ['name', 'surname', 'age', 'sex', 'department', 'language']


class DepartmentAPIViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
    search_fields = ['name']
    ordering_fields = ['name']


class ProgrammingLanguageAPIViewSet(ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializers
    search_fields = ['name']
    ordering_fields = ['name']
