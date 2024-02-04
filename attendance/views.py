from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Course, Attendance, Attendee
from django.contrib import messages
from .forms import CourseForm
from students.models import Student
from django.shortcuts import render, redirect



def CourseList(request):
    course = Course.objects.all().order_by('name')
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex)
    context = {'courses':course, 'CourseForm':CourseForm, 'sex':sex}
    return render(request, template_name='course_list.html', context=context)

#-- Create a course-#
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


def CourseDelete(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    messages.success(request, 'Deleted Successfully')

    return redirect('course_list')

#<<-- Attendance Views -->> 
def AttendanceList(request, pk):
    course = Course.objects.get(pk=pk)

    attendance = Attendance.objects.filter(course=pk).order_by('start_date')
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex) # the need for the profile picture

    context = {'attendances':attendance, 'course':course, 'sex':sex}
    return render(request, template_name='attendance_list.html', context=context)


def AttendanceCreate(request, pk):
    if request.method == 'POST':

        day_number = request.POST['daynumber']
        course = Course.objects.get(pk=pk)
        attendance_url = reverse('attendance_list', args=[course.id])
        try:
            new = Attendance.objects.create(course=course, day_number=day_number)
            new.save()
            message = 'Creation Success'
            messages.success(request, message)
            return redirect(attendance_url)
        
        except Exception as error:
            messages.warning(request, error)
            return redirect(attendance_url)

    else:
        return redirect('attendance_list')
    



def AttendanceDelete(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    course_pk = attendance.course.id
    attendance_url = reverse('attendance_list', args=[course_pk])
    try:
           
        attendance.delete()
        messages.success(request, 'Deleted Successfully')
        return redirect(attendance_url)
    
    except Exception as error:
        messages.warning(request, error)
        return redirect(attendance_url)



#<<-- Attendee Views -->
class AttendeeListView(ListView):
    model = Attendee
    template_name = 'attendee_list.html'
    context_object_name = 'attendees'

class AttendeeDetailView(DetailView):
    model = Attendee
    template_name = 'attendee_detail.html'
    context_object_name = 'attendee'

class AttendeeCreateView(CreateView):
    model = Attendee
    template_name = 'attendee_create.html'
    fields = '__all__'
    success_url = reverse_lazy('attendee_list')

class AttendeeUpdateView(UpdateView):
    model = Attendee
    template_name = 'attendee_update.html'
    fields = '__all__'
    success_url = reverse_lazy('attendee_list')

class AttendeeDeleteView(DeleteView):
    model = Attendee
    template_name = 'attendee_delete.html'
    success_url = reverse_lazy('attendee_list')
