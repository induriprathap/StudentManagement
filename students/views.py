from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login

from .models import Student
from .forms import StudentForm, RegisterForm


@login_required
@permission_required("students.view_student", raise_exception=True)
def student_list(request):

    search = request.GET.get("search", "")

    if search:
        students = Student.objects.filter(
            name__icontains=search
        )
    else:
        students = Student.objects.all()

    # Pagination
    paginator = Paginator(students, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "students/student_list.html",
        {
            "students": page_obj,
            "page_obj": page_obj
        }
    )


@login_required
@permission_required("students.add_student", raise_exception=True)
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student added successfully!"
            )

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form
        }
    )


@login_required
@permission_required("students.change_student", raise_exception=True)
def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student updated successfully!"
            )

            return redirect("student_list")

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "students/student_edit.html",
        {
            "form": form
        }
    )


@login_required
@permission_required("students.delete_student", raise_exception=True)
def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    messages.success(
        request,
        "Student deleted successfully!"
    )

    return redirect("student_list")


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Account created successfully!"
            )

            return redirect("student_list")

    else:

        form = RegisterForm()

    return render(
        request,
        "students/register.html",
        {
            "form": form
        }
    )