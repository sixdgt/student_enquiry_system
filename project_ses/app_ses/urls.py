from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_index, name="students.index"),
    path("students/create/", views.student_create, name="students.create"),
    path("students/edit/<int:id>/", views.student_edit, name="students.edit"),
    path("students/show/<int:id>/", views.student_show, name="students.show"),
    path("students/delete/<int:id>/", views.student_delete, name="students.delete"),
]