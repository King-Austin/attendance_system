from django.forms import ModelForm
from .models import Course

# Create the form class.
class CourseForm(ModelForm):
    class Meta:
        model=Course
        fields = ['name']