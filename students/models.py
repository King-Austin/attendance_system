from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    reg_number = models.CharField(unique=True, verbose_name='Registration Number', max_length =10)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name = 'Last Name')
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField(verbose_name = 'Date of Birth', null=True, blank=True)
    auth_code = models.CharField(max_length=20, verbose_name= 'Auth Code', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone',  null=True, blank=True)
    admin = models.CharField(max_length=20, verbose_name='Admin', default='False' null=True, blank=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

        def __str__(self) -> str:
            return f'{self.first_name}-{self.last_name}'
        
#-- CREATING THE AUTHENTICATED STUDENTS MODELS --#



