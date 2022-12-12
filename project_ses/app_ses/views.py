from django.shortcuts import render

# Create your views here.
def student_index(request):
    return render(request, "students/index.html")

def student_create(request):
    return render(request, "students/create.html")

def student_show(request):
    return render(request, "students/show.html")

def student_edit(request):
    return render(request, "students/edit.html")
    