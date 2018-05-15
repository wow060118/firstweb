from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import student,teacher
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

def vote (request,t_no):
    return HttpResponse("your teachet no is %s." % t_no)