from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=False)
    code = models.IntegerField(unique=True, blank=False)
    description = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class HOD(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='HOD', on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50,  blank=False)
    mobile = models.CharField(max_length=10,  blank=False)
    image = models.ImageField(upload_to='Images/HOD', blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, blank=False)
    code = models.IntegerField(unique=True, blank=False)
    description = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='Subject', on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50, blank=False)
    code = models.IntegerField(unique=True, blank=False)
    description = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='Faculty', on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, blank=False)
    mobile = models.CharField(max_length=10)
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='Images/Faculty', blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='Student', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='Student', on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, blank=False)
    father_name = models.CharField(max_length=50, blank=True)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    image = models.ImageField(upload_to='Images/Student', blank=True)

    def __str__(self):
        return self.name


class NoticeDepartment(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='NoticeDepartment', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class NoticeFaculty(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='NoticeFaculty', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class NoticeStudent(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, related_name='NoticeStudent', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class TimeTable(models.Model):
    department = models.ForeignKey(Department, related_name='TimeTable', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='Images/TimeTable', blank=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, related_name='Assignment', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
