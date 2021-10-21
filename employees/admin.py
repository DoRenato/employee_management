from django.contrib import admin
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','department','salary','birth_date')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'id')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)