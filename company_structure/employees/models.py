from django.db import models
from django.core.validators import MinValueValidator


class Department(models.Model):
    name = models.CharField(max_length=255)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='directed_department')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='employee_photos', null=True, blank=True)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        unique_together = ('name', 'department')

    def __str__(self):
        return self.name