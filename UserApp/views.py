from django.shortcuts import render,redirect
from datetime import datetime
from AdminApp.models import songDB
from UserApp.models import user_registerDB
from django.contrib import messages
from AdminApp.views import main_page
# Create your views here.
def index_user(req):
    x = datetime.now()
    songs=songDB.objects.count()
    return render(req,"index_user.html",{'x':x,'songs':songs})

def display_songs_user(req):
    song_data=songDB.objects.all()
    return render(req,"display_songs_user.html",{'song_data':song_data})
def user_register(req):
    return render(req,"user_registration.html")

def save_user_register(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('password')
        e=request.POST.get('confirmpwd')
        if user_registerDB.objects.filter(username=a).exists():
            messages.warning(request,"Username already exists..!")
        elif user_registerDB.objects.filter(email=b).exists():
            messages.warning(request,"Email Id already exists..!")
        obj=user_registerDB(username=a,email=b,mobile=c,password=d,confirmpwd=e)
        obj.save()
        return redirect(user_register)
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if user_registerDB.objects.filter(username=un,password=pwd).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            messages.success(request,"Welcome to User Dashboard...")
            return redirect(index_user)

        else:
            messages.warning(request, "Invalid Password...!")
            return redirect(user_register)
    else:
        messages.warning(request, "Invalid Credentials...!")
        return redirect(user_register)
def user_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...")
    return redirect(user_register)
