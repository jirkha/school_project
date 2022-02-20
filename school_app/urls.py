from django.urls import path

from . import views

urlpatterns = [
    path("hello_world", views.hello_world, name="hello_world"),
    path("subjects", views.list_subjects, name="list_subjects"),
    path("subjects/<int:pk>", views.subject_detail, name="subject_detail"),
    path("teachers", views.list_teachers, name="list_teachers"),
    path("teachers/<int:pk>", views.teacher_detail, name="teachers_detail")
]
