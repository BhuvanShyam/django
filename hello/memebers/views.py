from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def student_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'student_list.html', {'course': course, 'students': students})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('course_list')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def enroll_student(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            course.students.add(student)
            return redirect('student_list', course_id=course.id)
    else:
        form = StudentForm()
    return render(request, 'enroll_student.html', {'course': course, 'form': form})
