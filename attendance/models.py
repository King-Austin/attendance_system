from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name_choices =[
        ('ECE 321', 'ECE 321'),
        ('FEG 303', 'FEG 303'),
        ('ELE 311', 'ELE 311'),
        ('ECE 323', 'ECE 323'),
        ('ELE 341', 'ELE 341'),
        ('ECE 331', 'ECE 331'),
        ('ELE 343', 'ELE 343'),
        ('ELE 353', 'ELE 353'),         
         
    ]

    name = models.CharField(max_length=20, choices=name_choices)
    attendees = models.ManyToManyField("Attendee", verbose_name=("Attendance"))
    def __str__(self):
        return (self.name)
    
class Attendance(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    attendee = models.ForeignKey("Attendee", verbose_name=("Student"), on_delete=models.CASCADE)

    start_date = models.DateField(auto_now=True)
    start_time = models.TimeField(auto_now=True)
    day_number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return (f'{self.name}- Day {self.day_number}')
    
class Attendee(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    signed_time = models.TimeField(auto_now=True)

    def __str__(self):
        return (f'{self.student} -> {self.course} at:{self.signed_time}')
    
