from django.forms import ModelForm
from .models import Course, Attendance, Attendee

# Create the form class.
class CourseForm(ModelForm):
    class Meta:
        model=Course
        fields = ['name']

