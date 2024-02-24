from typing import Any
from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django import forms
from temp_app.forms import StudentForm 
# from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return render(request, 'index.html')

# turning a view into a class page
# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASED VIEW!')

class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION'
    #     return context

# how to use context dictionary
# This will provide a list of all the record
class SchoolListView(ListView):
    # return a list of school_list
    # we can use this variable to change the list 
    model = models.School
    context_object_name = 'schools'

# this will provide all the detail in a view
class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'temp_app/school_detail.html'
    context_object_name = 'school_detail'

# create a class that will help with creating view
class SchoolCreateView(CreateView):
    fields = ('name','principal', 'location')
    model = models.School

# create class to update view
class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

# create class to delete view
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("temp_app:list")

# add student
class StudentCreateView(CreateView):
    model = models.Student
    form_class = StudentForm
    template_name = 'temp_app/create_student.html'
    success_url = reverse_lazy("temp_app:list")

    

    