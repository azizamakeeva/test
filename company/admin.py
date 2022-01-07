from django.contrib import admin
from company.models import Employee, Department, ProgrammingLanguage

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(ProgrammingLanguage)
