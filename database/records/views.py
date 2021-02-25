from django.shortcuts import render,redirect
from .models import student
# Create your views here.
def home(request):
    data = student.objects.all()
    return render(request,'home.html',{'data': data})

def add(request):
    name_01 = request.POST['name']
    roll_01 = request.POST['roll']
    new_student = student(name = name_01,roll = roll_01)

    new_student.save()
    return redirect(home)