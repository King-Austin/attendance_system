from django.urls import reverse
from .models import Course, Attendance, Attendee
from django.contrib import messages
from .forms import CourseForm
from students.models import Student
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .decorator import student_admin_required


def CourseList(request):
    course = Course.objects.all().order_by('name')
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex)
    context = {'courses':course, 'CourseForm':CourseForm, 'sex':sex}
    return render(request, template_name='course_list.html', context=context)

#-- Create a course-#
@student_admin_required
def CourseCreate(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Successfully')
            return redirect('course_list')
        else:
            messages.warning(request, 'Course already Exist')
            return redirect('course_list')

    else:
        return redirect('course_list')

@student_admin_required
def CourseDelete(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    messages.success(request, 'Deleted Successfully')

    return redirect('course_list')

#<<-- Attendance Views -->>

def AttendanceList(request, pk):
    course = Course.objects.get(pk=pk)

    attendance = Attendance.objects.filter(course=pk).order_by('day_number')
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex) # the need for the profile picture

    context = {'attendances':attendance, 'course':course, 'sex':sex}
    return render(request, template_name='attendance_list.html', context=context)

@student_admin_required
def AttendanceCreate(request, pk):
    if request.method == 'POST':

        day_number = request.POST['daynumber']
        course = Course.objects.get(pk=pk)
        attendance_url = reverse('attendance_list', args=[course.id])
        try:
            new = Attendance.objects.create(course=course, day_number=day_number)
            new.save()
            message = f'DAY {day_number} Creation Success'
            messages.success(request, message)
            return redirect(attendance_url)
        
        except Exception as error:
            message = f'DAY {day_number} already Exist'
            messages.warning(request, message)
            return redirect(attendance_url)

    else:
        return redirect('attendance_list')
    


@student_admin_required
def AttendanceDelete(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    course_pk = attendance.course.id
    attendance_url = reverse('attendance_list', args=[course_pk])
    try:
           
        message = f'{attendance.course} -DAY {attendance.day_number} Delete Success'
        attendance.delete()
        messages.success(request, message)
        return redirect(attendance_url)
    
    except Exception as error:
        messages.warning(request, error)
        return redirect(attendance_url)

@student_admin_required
def AttendanceActivate(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    course_pk = attendance.course.id
    attendance_url = reverse('attendance_list', args=[course_pk])
    try:
           
        attendance.active = True
        attendance.save()
        message = f'{attendance.course} -DAY {attendance.day_number} Activated'
        messages.success(request, message)
        return redirect(attendance_url)
    
    except Exception as error:
        messages.warning(request, error)
        return redirect(attendance_url)

@student_admin_required
def AttendanceDeactivate(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    course_pk = attendance.course.id
    attendance_url = reverse('attendance_list', args=[course_pk])
    try:
           
        attendance.active = False
        attendance.save()
        message = f'{attendance.course} -DAY {attendance.day_number} Deactivated'
        messages.success(request, message)
        return redirect(attendance_url)
    
    except Exception as error:
        messages.warning(request, error)
        return redirect(attendance_url)



#<<-- Attendee Views -->
def AttendeeList(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    attendee = Attendee.objects.filter(attendance_id=pk).order_by('signed_time')
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex) # the need for the profile picture

    context = {'attendee':attendee, 'attendance':attendance, 'sex':sex}
    return render(request, template_name='attendee_list.html', context=context)



@student_admin_required
def AttendeeDelete(request, pk):
    attendee = Attendee.objects.get(pk=pk)
    attendee_url = reverse('attendee_list', args=[attendee.attendance.id])
    attendee.delete()
    return redirect(attendee_url)


@student_admin_required
def AttendeeCreate(request, pk):
    if request.method == 'POST':
        student_reg_number = request.POST['regnumber']
        attendance = Attendance.objects.get(pk=pk)
        attendee_url = reverse('attendee_list', args=[pk])

        user = User.objects.filter(username=student_reg_number).exists()
        if user:
            try:
                user = User.objects.get(username=student_reg_number)
                new_attendee = Attendee.objects.create(user=user, attendance=attendance)
                new_attendee.save()
                message = f'{student_reg_number}-{user.first_name} Added Successfully !'
                messages.success(request, message)
                return redirect(attendee_url)
            except Exception as error:
                message = f'{student_reg_number} already signed  !'
                messages.warning(request, message)
                return redirect(attendee_url)
        else:
            message = 'User Not Registered'
            messages.warning(request, message)
            return redirect(attendee_url)
    
    else:
        return redirect(attendee_url)

#----------Adminship Views ------------#
    
def StudentAdmin(request):

    admins = Student.objects.filter(admin=True).order_by('reg_number')
    context = {'admins':admins}
    return render(request, template_name='admins.html', context=context)


def StudentAdminCreate(request):
    if request.method == 'POST':
        student_reg_number = request.POST['regnumber']

        user = User.objects.filter(username=student_reg_number).exists()
        if user:
            try:
                admin = Student.objects.get(reg_number = student_reg_number)
                admin.admin = True
                admin.save()
                message = f'{student_reg_number}-{user.first_name} Added Successfully !'
                messages.success(request, message)
                return redirect('admin_list')
            except Exception as error:
                message = f'{student_reg_number} already signed  !'
                messages.warning(request, message)
                return redirect('admin_list')
        else:
            message = 'User Not Registered'
            messages.warning(request, message)
            return redirect('admin_list')
    
    else:
        return redirect('admin_list')

def StudentAdminDelete(request, pk):
    admin = Student.objects.get(id=pk)
    admin.admin=False
    admin.save()
    return redirect ('admin_list')


def PermissionDenied(request):
    return render(request, template_name='permission_denied.html')

def Development(request):
    return render(request, template_name='development.html')
