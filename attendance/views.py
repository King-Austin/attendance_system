from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_create.html'
    fields = '__all__'  # Or specify the fields you want to include
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update.html'
    fields = '__all__'  # Or specify the fields you want to include
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')
