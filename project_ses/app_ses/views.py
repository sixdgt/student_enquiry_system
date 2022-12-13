from django.shortcuts import render
from .forms import StudentCreateForm, CourseCreateForm, UserRegisterForm, UserLoginForm
# Create your views here.
def student_index(request):
    return render(request, "students/index.html")

def student_create(request):
    std_create_form = StudentCreateForm()
    context = {
        "temp_form": std_create_form
    }
    return render(request, "students/create.html", context)

def student_show(request):
    return render(request, "students/show.html")

def student_edit(request):
    return render(request, "students/edit.html")
    