from .views import *
from django.conf.urls import url

urlpatterns = [

    url(r'^course/(?P<pk>\d+)$', course, name='course'),

    url(r'^logout/$', logout, name='logout'),

    url(r'^edit_department/(?P<pk>\d+)$', edit_department, name="edit_department"),
    url(r'^edit_faculty/(?P<pk>\d+)$', edit_faculty, name="edit_faculty"),
    url(r'^edit_student/(?P<pk>\d+)$', edit_student, name="edit_student"),

    url(r'^deletedepartment/(?P<pk>\d+)$', deletedepartment, name="deletedepartment"),
    url(r'^deletestudent/(?P<pk>\d+)$', deletestudent, name="deletestudent"),
    url(r'^deletefaculty/(?P<pk>\d+)$', deletefaculty, name="deletefaculty"),

    url(r'^hod_login/$', hod_login, name='hod_login'),
    url(r'^faculty_login/$', faculty_login, name='faculty_login'),
    url(r'^student_login/$', student_login, name='student_login'),

    url(r'^student_page/$', student_page, name='student_page'),
    url(r'^faculty_page/$', faculty_page, name='faculty_page'),
    url(r'^hod_page/$', hod_page, name='hod_page'),

    url(r'^show_studentlist/$', show_studentlist, name='show_studentlist'),
    url(r'^show_facultylist/$', show_facultylist, name='show_facultylist'),

    url(r'^add_noticedepartment$', add_noticedepartment, name="add_noticedepartment"),
    url(r'^add_noticefaculty$', add_noticefaculty, name="add_noticefaculty"),
    url(r'^add_noticestudent$', add_noticestudent, name="add_noticestudent"),

    url(r'^showdepartmenthod/(?P<pk>\d+)$', showdepartmenthod, name='showdepartmenthod'),
    url(r'^showfacultyhod/(?P<pk>\d+)$', showfacultyhod, name='showfacultyhod'),
    url(r'^showstudenthod/(?P<pk>\d+)$', showstudenthod, name='showstudenthod'),

    url(r'^showdepartmentfaculty/(?P<pk>\d+)$', showdepartmentfaculty, name='showdepartmentfaculty'),
    url(r'^showfacultyfaulty/(?P<pk>\d+)$', showfacultyfaulty, name='showfacultyfaulty'),
    url(r'^showstudentfaculty/(?P<pk>\d+)$', showstudentfaculty, name='showstudentfaculty'),

    url(r'^showdepartmentstudent/(?P<pk>\d+)$', showdepartmentstudent, name='showdepartmentstudent'),
    url(r'^showfacultystudent/(?P<pk>\d+)$', showfacultystudent, name='showfacultystudent'),
    url(r'^showstudentstudent/(?P<pk>\d+)$', showstudentstudent, name='showstudentstudent'),

    url(r'^sms_faculty/(?P<pk>\d+)$', sms_faculty, name='sms_faculty'),
    url(r'^sms_student/(?P<pk>\d+)$', sms_student, name='sms_student'),

    url(r'^upload_timetable/$', upload_timetable, name='upload_timetable'),
    url(r'^show_timetable/$', show_timetable, name='show_timetable'),

    url(r'^assignment/$', assignment, name='assignment'),
    url(r'^add_assignment/$', add_assignment, name='add_assignment'),

    url(r'^$', index, name='index'),
]