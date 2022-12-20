from django.shortcuts import render, redirect
from .forms import StudentCreateForm, CourseCreateForm, UserRegisterForm, UserLoginForm
from .models import Course, Student, AppUser
from django.core.mail import send_mail

# Create your views here.
def user_register(request):
    reg_form = UserRegisterForm()
    context = {"form": reg_form}
    if request.method == "POST":
        user_form_data = UserRegisterForm(request.POST)
        if user_form_data.is_valid():
            user_form_data.save()
            send_mail(
                "User Registration", # subject
                "Congratulations! Your account has been created", # message
                "c4crypt@gmail.com", # sender
                [request.POST.get('email')] # receiver
            )
            return redirect("users.login")
        else:
            return redirect("users.register")
    return render(request, "users/register.html", context)

def user_login(request):
    login_form = UserLoginForm()
    context = {"form": login_form}
    if request.method == "POST":
        req_email = request.POST.get("email")
        req_password = request.POST.get("password")
        user_data = AppUser.objects.get(email=req_email)
        if user_data.email == req_email and user_data.password == req_password:
            request.session["session_email"] = user_data.email
            return redirect("students.index")
        else:
            return redirect("users.login")
    return render(request, "users/login.html", context)

def student_index(request):
    if not request.session.has_key("session_email"):
        return redirect("users.login")
    std_list = Student.objects.all()
    context = {"std_list": std_list}
    return render(request, "students/index.html", context)

def student_create(request):
    if not request.session.has_key("session_email"):
        return redirect("users.login")
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

def student_update(request):
    if not request.session.has_key("session_email"):
        return redirect("users.login")
    if request.method == "POST":
        course = Course.objects.get(id=request.POST.get("course_id"))
        std_obj = Student.objects.get(id=request.POST.get('id'))
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
    
    return redirect("students.index")

def student_show(request, id):
    if not request.session.has_key("session_email"):
        return redirect("users.login")
    data = Student.objects.get(id=id)
    context = {"data": data}
    return render(request, "students/show.html", context)

def student_edit(request, id):
    if not request.session.has_key("session_email"):
        return redirect("users.login")
    data = Student.objects.get(id=id)
    courses = Course.objects.all()
    context = {"data": data, "courses": courses}
    return render(request, "students/edit.html", context)

def student_delete(request, id):
    if not request.session.has_key("session_email"):
        return redirect("users.login")
    data = Student.objects.get(id=id)
    data.delete()
    return redirect("students.index")
    