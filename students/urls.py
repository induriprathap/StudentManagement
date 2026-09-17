from django.urls import path
from django.contrib.auth import views as auth_views
from .api_views import student_api

from .views import (
    student_list,
    add_student,
    edit_student,
    delete_student,
    register
)


urlpatterns = [

    # Login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="students/login.html"
        ),
        name="login"
    ),


    # Logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),


    # Registration
    path(
        "register/",
        register,
        name="register"
    ),


    # Student List
    path(
        "",
        student_list,
        name="student_list"
    ),


    # Add Student
    path(
        "add/",
        add_student,
        name="add_student"
    ),


    # Edit Student
    path(
        "edit/<int:id>/",
        edit_student,
        name="edit_student"
    ),


    # Delete Student
    path(
        "delete/<int:id>/",
        delete_student,
        name="delete_student"
    ),
    path(
    "api/students/",
    student_api,
    name="student_api"
),

]