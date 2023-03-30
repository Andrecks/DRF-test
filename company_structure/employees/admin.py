from django.contrib import admin
from .models import Employee, Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'department')
    list_filter = ('department',)
    search_fields = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'director')
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)