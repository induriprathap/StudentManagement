from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'course']

    def clean_age(self):
        age = self.cleaned_data['age']

        if age <= 0:
            raise forms.ValidationError(
                "Age must be greater than 0."
            )

        return age

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only letters."
            )

        return name

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                "Please enter a Gmail address."
            )

        return email

    def clean_course(self):
        course = self.cleaned_data['course']

        if not course:
            raise forms.ValidationError(
                "Please select a course."
            )

        return course


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']