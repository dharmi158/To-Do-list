from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
       
        user = auth.authenticate(username = request.POST['username'] , password = request.POST['password'] )
        if user is not None:
            auth.login(request,user)
            return render(request, 'showdiary.html')
        else:
            return render(request,'home.html' , {'error' : "INVALID LOGIN CREDENTIALS"})
    else:
        return render(request,'home.html')

def signup(request):
    if request.method == "POST":
      if request.POST['password']==request.POST['passwordagain']:
          try:
              user = User.objects.get(username = request.POST['username'])
              return render(request, 'register.html' , {'error': "USERNAME HAS ALREADY BEEN TAKEN"})
          except User.DoesNotExist:
              user = User.objects.create_user(username=request.POST['username'] ,password=request.POST['password'])
              auth.login(request , user)
              return redirect(home)
      else:
          return render(request, 'register.html' , {'error': "PASSWORDS DON'T MATCH "})
    else:
        return render(request , 'register.html')



def logout(request):
    auth.logout(request)
    return redirect(home)