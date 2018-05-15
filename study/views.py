import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import student,teacher
from django.core import serializers
from django.db import connection


# Create your views here.
def index(request):
    latest_student_list = student.objects.order_by('-id')[:5]
    context ={'latest_student_list':latest_student_list}
    return render(request,'study/index.html',context)

def detail (request,s_id):
    s = get_object_or_404(student, pk=s_id)
    return render(request,'study/detail.html',{"student":s})

def results (request, s_name):
    response = "your student name is %s."
    return HttpResponse(response % s_name)

#sql 操作
def vote (request,t_no):
    # s = student.objects.create(no=1, name="fff")
    # s1 = student()
    # s1.no = 123
    # s1.name = "ggg"
    # s1.save()
    sss = student.objects.raw("select * from study_student")
    print(serializers.serialize("json",sss))
    cursor = connection.cursor()
    cursor.execute('select * from study_student')
    runquery('select * from study_student')
    print(json.dumps(dictfetchall(cursor)))
    student.objects.filter(id=1).delete()
    student.objects.filter(id=2).update(name="qwer")

    return HttpResponse("your teachet no is %s." % t_no)

def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def runquery(sql):
    cursor = connection.cursor()
    cursor.execute(sql,None)
    col_names = [desc[0] for desc in cursor.description]
    print(col_names)
    row=cursor.fetchone()
    row = dict(zip(col_names, row))
    print(row)
