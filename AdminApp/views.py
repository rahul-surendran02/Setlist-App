from django.shortcuts import render,redirect
from AdminApp.models import songDB,admin_registerDB
from django.contrib import messages
from datetime import datetime
from UserApp.models import user_registerDB

# Create your views here.
def index(req):
    x = datetime.now()
    songs = songDB.objects.count()
    users= user_registerDB.objects.count()
    return render(req,"index.html",{'x':x,'songs':songs,'users':users})
def add_songs(req):
    return render(req,"add_songs.html")
def save_songs(request):
    if request.method=="POST":
        action = request.POST.get('action')

        if action == "Cancel":
            messages.info(request, "Song addition cancelled.")
            return redirect('add_songs')
        
        a=request.POST.get('date') or None
        b=request.POST.get('song')
        c=request.POST.get('des')
        obj=songDB(date=a,song=b,des=c)
        obj.save()
        messages.success(request,"your song saved successfully...!")
        return redirect(index)

def display_songs_admin(req):
    song_data=songDB.objects.all()
    return render(req,"display_songs_admin.html",{'song_data':song_data})
def edit_songs(req,song_id):
    song_data=songDB.objects.get(id=song_id)
    return render(req,"edit_songs.html",{'song_data':song_data})
def update_songs(req,song_id):
    if req.method=="POST":

        action = req.POST.get('action')

        if action == "Cancel":
            messages.info(req, "Song updation cancelled.")
            return redirect('edit_songs', song_id=song_id)
        
        a = req.POST.get('date')
        b = req.POST.get('song')
        c = req.POST.get('des')
        # try:
        #     img=req.FILES['image']
        #     fs=FileSystemStorage()
        #     file=fs.save(img.name,img)
        # except MultiValueDictKeyError:
        #     file=categoryDB.objects.get(id=cat_ID).cat_image
        songDB.objects.filter(id=song_id).update(date=a,song=b,des=c)
        messages.success(req, "song details updated successfully...!")
        return redirect(display_songs_admin)
def delete_songs(req,del_song_ID):
    x=songDB.objects.filter(id=del_song_ID)
    x.delete()
    messages.error(req, "song deleted...!")
    return redirect(display_songs_admin)


def admin_register(request):
    return render(request,"admin_registration.html")
def save_admin_register(request):
    admin_count = admin_registerDB.objects.count()
    # if admin_count = 1:
    #     messages.error(request, "Only one admin is allowed in the system. Contact support.")
    #     return redirect(admin_register)
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('password')
        e=request.POST.get('confirmpwd')
        if admin_registerDB.objects.filter(username=a).exists():
            messages.warning(request,"Username already exists..!")
        elif admin_registerDB.objects.filter(email=b).exists():
            messages.warning(request,"Email Id already exists..!")
        obj=admin_registerDB(username=a,email=b,mobile=c,password=d,confirmpwd=e)
        obj.save()
        return redirect(admin_register)
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if admin_registerDB.objects.filter(username=un,password=pwd).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            messages.success(request,"Welcome to Admin Dashboard...")
            return redirect(index)

        else:
            messages.warning(request, "Invalid Password...!")
            return redirect(admin_register)
    else:
        messages.warning(request, "Invalid Credentials...!")
        return redirect(admin_register)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...")
    return redirect(admin_register)

def main_page(req):
    return render(req,"main_page.html")