from django.shortcuts import render,redirect
from Home.models import contact,projects,subscribe

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['phonenumber']
        email = request.POST['email']
        msg = request.POST['message']

        cm = contact.objects.create(name=name,contact_num=number,email=email,message=msg)
        cm.save()

        return redirect('home')

    else:
        clients = projects.objects.all()
        return render(request,'index.html',{'clients':clients})

def subscribes(request):
    if request.method == "POST":
        email = request.POST['email']
        user = subscribe.objects.create(email=email)
        user.save()
        return redirect('home')

    else:
        return redirect('home')