from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course

def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = CourseForm()
    return render(request, 'create.html', {'form':form})
