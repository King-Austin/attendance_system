from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course, Attendance, Attendee
from django.contrib import messages
from .forms import CourseForm
from django.shortcuts import render, redirect



def CourseList(request):
    course = Course.objects.all().order_by('name')
    context = {'courses':course, 'CourseForm':CourseForm}
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

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update.html'
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')

#<<-- Attendance Views -->> 
class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list.html'
    context_object_name = 'attendances'

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'
    context_object_name = 'attendance'

class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = 'attendance_create.html'
    fields = '__all__'
    success_url = reverse_lazy('attendance_list')

class AttendanceUpdateView(UpdateView):
    model = Attendance
    template_name = 'attendance_update.html'
    fields = '__all__'
    success_url = reverse_lazy('attendance_list')

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'attendance_delete.html'
    success_url = reverse_lazy('attendance_list')

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
