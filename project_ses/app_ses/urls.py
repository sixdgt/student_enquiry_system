from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_index, name="students.index"),
    path("students/create/", views.student_create, name="students.create"),
    path("students/edit/", views.student_edit, name="students.edit"),
    path("students/show/", views.student_show, name="students.show"),
]