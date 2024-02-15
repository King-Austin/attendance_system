from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from functools import wraps

def student_admin_required(view_func):
    @wraps (view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated as a student
        if not request.user.is_authenticated:
            message = 'Kindly Authenticate'
            messages.success(request, message)
            return redirect('login')

        # Check if student record has is_admin flag set to True
        student = Student.objects.get(reg_number= request.user.username)
        if not student.admin:
            return redirect('permission_denied')

        # All conditions met, proceed to the view function
        return view_func(request, *args, **kwargs)

    return wrapper