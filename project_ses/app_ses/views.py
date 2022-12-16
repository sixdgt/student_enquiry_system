from django.shortcuts import render, redirect
from .forms import StudentCreateForm, CourseCreateForm, UserRegisterForm, UserLoginForm
from .models import Course, Student, AppUser

# Create your views here.
def student_index(request):
    std_list = Student.objects.all()
    context = {"std_list": std_list}
    return render(request, "students/index.html", context)

def student_create(request):
    std_create_form = StudentCreateForm()
    context = {
        "temp_form": std_create_form
    }

    if request.method == "POST":
        course = Course.objects.get(id=request.POST.get("course"))
        std_obj = Student()
        std_obj.first_name = request.POST.get("first_name")
        std_obj.middle_name = request.POST.get("middle_name")
        std_obj.last_name = request.POST.get("last_name")
        std_obj.email = request.POST.get("email")
        std_obj.contact = request.POST.get("contact")
        std_obj.gender = request.POST.get("gender")
        std_obj.blood_group = request.POST.get("blood_group")
        std_obj.academic_level = request.POST.get("academic_level")
        std_obj.academic_status = request.POST.get("academic_status")
        std_obj.academic_org = request.POST.get("academic_org")
        std_obj.academic_score = request.POST.get("academic_score")
        std_obj.course = course
        std_obj.intake = request.POST.get("intake")
        std_obj.shift = request.POST.get("shift")
        std_obj.remarks = request.POST.get("remarks")
        std_obj.save()
    
        context.setdefault("msg", "Student Added Successfully")

    return render(request, "students/create.html", context)

def student_show(request, id):
    data = Student.objects.get(id=id)
    context = {"data": data}
    return render(request, "students/show.html", context)

def student_edit(request, id):
    data = Student.objects.get(id=id)
    context = {"data": data}
    return render(request, "students/edit.html", context)

def student_delete(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect("students.index")
    