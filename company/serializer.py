from rest_framework import serializers

from company.models import Employee, Department, ProgrammingLanguage


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id', 'name', 'surname', 'age', 'sex', 'department', 'language',
        )


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id', 'name', 'floor',
        )


class ProgrammingLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = (
            'id', 'name',
        )
