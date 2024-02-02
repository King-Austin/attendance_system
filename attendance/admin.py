from django.contrib import admin
from .models import Course, Attendance, Attendee
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    
    list_display = ['name']



@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    
    list_display = ['attendee', 'start_date', 'start_time', 'day_number']



@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    
    list_display = ['student','signed_time']

