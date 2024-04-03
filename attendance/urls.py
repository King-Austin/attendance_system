

from django.urls import path
from .views import (
    CourseList, CourseCreate, CourseDelete,
    AttendanceList, AttendanceCreate, AttendanceActivate, AttendanceDeactivate, AttendanceDelete,
    AttendeeList, AttendeeCreate, AttendeeDelete, PermissionDenied, Development, StudentAdmin, StudentAdminCreate, StudentAdminDelete
)

urlpatterns = [
    # Course URLs
    path('courses/', CourseList, name='course_list'),
    path('courses/create/', CourseCreate, name='course_create'),
    path('courses/<int:pk>/delete/', CourseDelete, name='course_delete'),

    # Attendance URLs
    path('attendances/<int:pk>/', AttendanceList, name='attendance_list'),
    path('attendances/<int:pk>/create/', AttendanceCreate, name='attendance_create'),
    path('attendances/<int:pk>/delete/', AttendanceDelete, name='attendance_delete'),
    path('attendances/<int:pk>/activate/', AttendanceActivate, name='attendance_activate'),
    path('attendances/<int:pk>/deactivate/', AttendanceDeactivate, name='attendance_deactivate'),


    # Attendee URLs
    path('attendees/<int:pk>/', AttendeeList, name='attendee_list'),
    path('attendees/<int:pk>/create/', AttendeeCreate, name='attendee_create'),
    path('attendees/<int:pk>/delete/', AttendeeDelete, name='attendee_delete'),

    #Permission Denied URLs
    path('permission_denied/', PermissionDenied, name='permission_denied'),
    path('work_in_progress/', Development, name='development'),

    #Admins URLs
    path('student_admins/', StudentAdmin, name='admin_list'),
    path('student_admins/create/', StudentAdminCreate, name='admin_create'),
    path('student_admins/<int:pk>/delete/', StudentAdminDelete, name='admin_delete')

]
