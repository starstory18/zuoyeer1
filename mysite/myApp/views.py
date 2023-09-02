from django.http import HttpResponse

from myApp.models import Teacher
from django.shortcuts import render

import os
import csv


def index(request):
    list = Teacher.objects.all()
    context = {"teachers_list": list}
    return render(request, "myApp/index.html", context)

def search(request):
    name_name = request.POST["dname"]
    list = Teacher.objects.filter(name=name_name)
    context = {"teachers_list": list}
    return render(request, "myApp/teacher_result.html", context)

def search1(request):
    department_name = request.POST["department"]
    list = Teacher.objects.filter(department=department_name)
    context = {"teachers_list": list}
    return render(request, "myApp/search.html", context)



