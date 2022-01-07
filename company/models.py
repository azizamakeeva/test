from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return f'{self.name}'


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=258, blank=True, null=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    surname = models.CharField(max_length=128, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.BooleanField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='department', blank=True, null=True)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE,
                                 related_name='prlanguage', blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.surname} {self.name}'
