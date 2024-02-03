from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Course(models.Model):
    name_choices = settings.COURSE_LIST

    name = models.CharField(max_length=255, choices=name_choices)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    day_number = models.PositiveIntegerField(default=1)
    start_date = models.DateField(auto_now=True)
    start_time = models.TimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        unique_together = ['course', 'day_number']
    def __str__(self):
        return f'{self.course} - Day {self.day_number}'

#May be neccessary soonner
 #   def duration(self):
  #      return self.end_time - self.start_time
    
    def total_attendees(self):
        return self.attendee_set.count()
    
#-- Attendance Class -- #

class Attendee(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    signed_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ['attendance', 'user']