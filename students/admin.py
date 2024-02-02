from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    
    list_display = ['reg_number', 'first_name', 'last_name', 'sex', 'birth_date', 'auth_code', 'phone', 'admin']
