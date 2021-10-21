from django.contrib import admin
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','department','salary','birth_date')

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)