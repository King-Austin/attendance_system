

from django.urls import path
from .views import (
    CourseList, CourseCreate, CourseDeleteView,
    AttendanceListView, AttendanceCreateView, AttendanceDeleteView,
    AttendeeListView, AttendeeCreateView, AttendeeDeleteView
)

urlpatterns = [
    # Course URLs
    path('courses/', CourseList, name='course_list'),
    path('courses/create/', CourseCreate, name='course_create'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    # Attendance URLs
    path('attendances/', AttendanceListView.as_view(), name='attendance_list'),
    #path('attendances/<int:pk>/', AttendanceDetailView.as_view(), name='attendance_detail'),
    path('attendances/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    #path('attendances/<int:pk>/update/', AttendanceUpdateView.as_view(), name='attendance_update'),
    path('attendances/<int:pk>/delete/', AttendanceDeleteView.as_view(), name='attendance_delete'),

    # Attendee URLs
    path('attendees/', AttendeeListView.as_view(), name='attendee_list'),
    #path('attendees/<int:pk>/', AttendeeDetailView.as_view(), name='attendee_detail'),
    path('attendees/create/', AttendeeCreateView.as_view(), name='attendee_create'),
    #path('attendees/<int:pk>/update/', AttendeeUpdateView.as_view(), name='attendee_update'),
    path('attendees/<int:pk>/delete/', AttendeeDeleteView.as_view(), name='attendee_delete'),
]
