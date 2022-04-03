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

def retrieve_course(request):
    courses = Course.objects.all()
    return render(request,'search.html',{'courses':courses} )

def update_course(request,pk):
    courses = Course.objects.get(id=pk)
    form = CourseForm(instance=courses)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'courses': coursess,
        'form': form,
    }
    return render(request,'update.html',context)

def delete_course(request, pk):
    courses = Course.objects.get(id=pk)

    if request.method == 'POST':
        courses.delete()
        return redirect('/search')

    context = {
        'courses': courses,
    }
    return render(request, 'remove.html', context)