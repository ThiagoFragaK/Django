from django import forms
from django.forms import ModelForm
from .models import Blog, Course

class CourseForm(forms.ModelForm):  
    class Meta:  
        model = Course
        fields = "__all__" 