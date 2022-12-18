from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())


class NoticeDepartmentForm(forms.ModelForm):
    class Meta:
        model = NoticeDepartment
        fields = ('department', 'title', 'description')


class NoticeFacultyForm(forms.ModelForm):
    class Meta:
        model = NoticeFaculty
        fields = ('department', 'title', 'description')


class NoticeStudentForm(forms.ModelForm):
    class Meta:
        model = NoticeStudent
        fields = ('department', 'title', 'description')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ('department', 'name', 'image')


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('subject', 'name', 'description')


class HoldForm(forms.Form):
    Enter = forms.CharField(max_length=200)


