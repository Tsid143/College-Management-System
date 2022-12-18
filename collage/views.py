from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from http import client
from .forms import *
from .models import *
from django.contrib import messages
import http
import json


def index(request):
    items = Department.objects.all()
    context = {
        'items': items,
        'header': 'Department',
    }
    return render(request, 'index.html', context)


def cours(request, pk, model):
    item = get_object_or_404(model, pk=pk)
    items = Course.objects.filter(department__name__exact=item.name)
    hold = HOD.objects.filter(department__name__exact=item.name)

    context = {
        'items': items,
        'header': item.name,
        'hold': hold,
    }
    return render(request, 'department.html', context)


def course(request, pk):
    return cours(request, pk, Department)


def hodnotic(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    items = cls.objects.filter(department__name__exact=item.department)
    if cls == NoticeDepartment:
        context = {
            'items': items,
            'header': 'DepartmentNotice'
        }
    if cls == NoticeFaculty:
        context = {
            'items': items,
            'header': 'FacultyNotice'
        }
    if cls == NoticeStudent:
        context = {
            'items': items,
            'header': 'StudentNotice'
        }
    messages.success(request, "Load Successfully")
    return render(request, 'notice.html', context)


def showdepartmenthod(request, pk):
    return hodnotic(request, pk, HOD, NoticeDepartment)


def showfacultyhod(request, pk):
    return hodnotic(request, pk, HOD, NoticeFaculty)


def showstudenthod(request, pk):
    return hodnotic(request, pk, HOD, NoticeStudent)


def facultynotic(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    items = cls.objects.filter(department__name__exact=item.department)
    if cls == NoticeDepartment:
        context = {
            'items': items,
            'header': 'DepartmentNotice'
        }
    if cls == NoticeFaculty:
        context = {
            'items': items,
            'header': 'FacultyNotice'
        }
    if cls == NoticeStudent:
        context = {
            'items': items,
            'header': 'StudentNotice'
        }
    messages.success(request, "Load Successfully")
    return render(request, 'noticefaculty.html', context)


def showdepartmentfaculty(request, pk):
    return facultynotic(request, pk, HOD, NoticeDepartment)


def showfacultyfaulty(request, pk):
    return facultynotic(request, pk, HOD, NoticeFaculty)


def showstudentfaculty(request, pk):
    return facultynotic(request, pk, HOD, NoticeStudent)


def studentnotic(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    items = cls.objects.filter(department__name__exact=item.department)
    if cls == NoticeDepartment:
        context = {
            'items': items,
            'header': 'DepartmentNotice'
        }
    if cls == NoticeFaculty:
        context = {
            'items': items,
            'header': 'FacultyNotice'
        }
    if cls == NoticeStudent:
        context = {
            'items': items,
            'header': 'StudentNotice'
        }
    messages.success(request, "Load Successfully")
    return render(request, 'noticestudent.html', context)


def showdepartmentstudent(request, pk):
    return studentnotic(request, pk, HOD, NoticeDepartment)


def showfacultystudent(request, pk):
    return studentnotic(request, pk, HOD, NoticeFaculty)


def showstudentstudent(request, pk):
    return studentnotic(request, pk, HOD, NoticeStudent)



def edit_allnotic(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            items = model.objects.filter(department__name__exact=item.department)
            if model == NoticeDepartment:
                context = {
                    'items': items,
                    'header': 'DepartmentNotice'
                }
            if model == NoticeFaculty:
                context = {
                    'items': items,
                    'header': 'FacultyNotice'
                }
            if model == NoticeStudent:
                context = {
                    'items': items,
                    'header': 'StudentNotice'
                }

            messages.success(request, "Updated")
            return render(request, 'notice.html', context)
    else:
        form = cls(instance=item)

        return render(request, 'editallnotice.html', {'form': form})


def edit_department(request, pk):
    return edit_allnotic(request, pk, NoticeDepartment, NoticeDepartmentForm)


def edit_faculty(request, pk):
    return edit_allnotic(request, pk, NoticeFaculty, NoticeFacultyForm)


def edit_student(request, pk):
    return edit_allnotic(request, pk, NoticeStudent, NoticeStudentForm)


def delet(request, pk, cls):
    item = get_object_or_404(cls, pk=pk)
    cls.objects.filter(id=pk).delete()
    messages.success(request, "Successfully deleted")
    items = cls.objects.filter(department__exact=item.department)
    if cls == NoticeDepartment:
        context = {
            'items': items,
            'header': 'DepartmentNotice'
        }
    if cls == NoticeFaculty:
        context = {
            'items': items,
            'header': 'FacultyNotice'
        }
    if cls == NoticeStudent:
        context = {
            'items': items,
            'header': 'StudentNotice'
        }
    return render(request, 'notice.html', context)


def deletedepartment(request, pk):
    return delet(request, pk, NoticeDepartment)


def deletefaculty(request, pk):
    return delet(request, pk, NoticeFaculty)


def deletestudent(request, pk):
    return delet(request, pk, NoticeStudent)


def logout(request):
    messages.success(request, "Successfully Logged Out")
    return render(request, 'index.html')


def faculty_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            dbuser = Faculty.objects.filter(username=un, password=pw)
            if not dbuser:
                messages.warning(request, 'Invalid User.')
                return redirect('faculty_login')
            else:
                item = Faculty.objects.filter(username__exact=un)
                for i in item:
                    tt = i.department
                context = {
                    'it': item,
                    'header': tt
                }
                messages.success(request, "Login Successfully")
                return render(request, 'facultypage.html', context)
    else:
        form = LoginForm()
        return render(request, 'facultylogin.html', {'form': form, 'header': 'Login'})


def student_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            dbuser = Student.objects.filter(username=un, password=pw)
            if not dbuser:
                messages.warning(request, 'Invalid User.')
                return redirect('student_login')
            else:
                item = Student.objects.filter(username__exact=un)
                for i in item:
                    tt = i.department
                context = {
                    'it': item,
                    'header': tt
                }
                messages.success(request, "Login Successfully")
                return render(request, 'studentpage.html', context)
    else:
        form = LoginForm()
        return render(request, 'studentlogin.html', {'form': form, 'header': 'Login'})


def hod_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            dbuser = HOD.objects.filter(username=un, password=pw)
            if not dbuser:
                messages.warning(request, 'Invalid User.')
                return redirect('hod_login')
            else:
                item = HOD.objects.filter(username__exact=un)
                for i in item:
                    tt = i.department
                context = {
                    'hold': item,
                    'header': tt
                }
                messages.success(request, "Login Successfully")
                return render(request, 'hodpage.html', context)
    else:
        form = LoginForm()
        return render(request, 'hodlogin.html', {'form': form, 'header': 'Login'})


def add_notic(request, cls):
    if request.method == "POST":
        form = cls(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Notice Saved Successfully")
            return render(request, 'addnotice.html')

    else:
        form = cls()
        return render(request, 'addnotice.html', {'form': form})


def add_noticedepartment(request):
    return add_notic(request, NoticeDepartmentForm)


def add_noticefaculty(request):
    return add_notic(request, NoticeFacultyForm)


def add_noticestudent(request):
    return add_notic(request, NoticeStudentForm)


def hod_page(request):
    return render(request, 'hodpage.html')


def faculty_page(request):
    return render(request, 'facultypage.html')


def student_page(request):
    return render(request, 'studentpage.html')


def sms(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    items = cls.objects.filter(department__name__exact=item.department)
    if request.method == 'POST':
        smsform = HoldForm(request.POST)
        if smsform.is_valid():
            msg = request.POST["Enter"]
            for i in items:
                mobno = i.mobile
                print(i.mobile)
                conn = http.client.HTTPConnection("api.msg91.com")
                payload = "{ \"sender\":\"Taosif\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\":\"" + msg + "\",\"to\": [ \"" + mobno + "\" ] } ] }"
                headers = {
                    'authkey': "270138ALh2WwCTXf5ca059c9",
                    'content-type': "application/json"
                }
                conn.request("POST", "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&afterminutes=&response=&campaign=", payload, headers)
                data = conn.getresponse()
                res = json.loads(data.read().decode("utf-8"))
                print(res)

            if res["type"] == "success":
                messages.success(request, "Successfully Send")
                return render(request, 'hodpage.html', {'header': 'Sms'})
            else:
                messages.success(request, "Not Successfully Send")
                return render(request, 'hodpage.html', {'header': 'Sms'})

        else:
            return render(request, 'sms.html', {'smsform': smsform, 'header': 'Sms'})
    else:
        smsform = HoldForm()
        return render(request, 'sms.html', {'smsform': smsform, 'header': 'Sms'})


def sms_faculty(request, pk):
    return sms(request, pk, HOD, Faculty)


def sms_student(request, pk):
    return sms(request, pk, HOD, Student)


def upload_timetable(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            item = TimeTable.objects.all()
            context = {
                'items': item,
            }
            return render(request, 'timetable.html', context)
    else:
        form = DocumentForm()
        item = TimeTable.objects.all()
        return render(request, 'timetable.html', {'form': form, 'header': 'Time_Table', 'items': item})


def show_facultylist(request):
    if request.method == 'POST':
        form = HoldForm(request.POST)
        if form.is_valid():
            t = request.POST["Enter"]
            print(t)
            item = Faculty.objects.filter(department__name__exact=t)
            context = {
                'items': item,
                'header': 'FacultyList'
            }
            return render(request, 'facultylist.html', context)
    else:
        form = HoldForm()
        return render(request, 'facultylist.html', {'form': form, 'header': 'FacultyList'})


def show_studentlist(request):
    if request.method == 'POST':
        form = HoldForm(request.POST)
        if form.is_valid():
            t = request.POST["Enter"]
            print(t)
            item = Student.objects.filter(course__name__exact=t)
            context = {
                'items': item,
                'header': 'StudentList'
            }
            return render(request, 'studentlist.html', context)
    else:
        form = HoldForm()
        return render(request, 'studentlist.html', {'form': form, 'header': 'Time_Table'})


def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added")
            return render(request, 'addassignment.html')
    else:
        form = AssignmentForm()
        return render(request, 'addassignment.html', {'form': form, 'header': 'Assignment'})


def assignment(request):
    if request.method == 'POST':
        form = HoldForm(request.POST)
        if form.is_valid():
            t = request.POST["Enter"]
            print(t)
            item = Assignment.objects.filter(subject__name__exact=t)
            context = {
                'items': item,
                'header': 'Assignment'
            }
            return render(request, 'assignment.html', context)
    else:
        form = HoldForm()
        return render(request, 'assignment.html', {'form': form, 'header': 'Assignment'})


def show_timetable(request):
    if request.method == 'POST':
        form = HoldForm(request.POST)
        if form.is_valid():
            t = request.POST["Enter"]
            print(t)
            item = TimeTable.objects.filter(department__name__exact=t)
            context = {
                'items': item,
                'header': 'TimeTable'
            }
            return render(request, 'showtimetable.html', context)
    else:
        form = HoldForm()
        return render(request, 'showtimetable.html', {'form': form, 'header': 'Time_Table'})