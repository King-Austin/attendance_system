from django.contrib import admin
from .models import Course, Attendance, Attendee
# Register your models here.

'''
adm.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Attendee)
'''


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    
    list_display = ['name']



@admin.register(Attendance)

class AttendanceAdmin(admin.ModelAdmin):
    
   list_display = ['course', 'start_date', 'start_time', 'day_number', 'active']

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    
    list_display = ['attendance', 'user', 'signed_time']

