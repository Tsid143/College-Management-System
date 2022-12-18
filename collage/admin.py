from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Department, HOD, Course, Subject, Faculty, Student, NoticeDepartment, NoticeFaculty, NoticeStudent, TimeTable)
class ViewAdmin(ImportExportModelAdmin):
    pass
