from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, RegistrationData
from .forms import RegistrationForm, RegistrationModel
from django.contrib import messages
# Create your views here.

def Home(request):
    context = {
        "name":"Syed"
    }
    return render(request, 'home.html', context)

def NewsP(request):
    # gets the data from database with id = 1
    obj = News.objects.get(id=1)

    context = {
        "list": ["Python", "javascript", "Ruby", "C#"],
        "num": 30,
        "data": obj
    }
    print(obj.title)
    return render(request,"news.html", context)

def Contact(request):
    return render(request, "contact.html")

def Register(request):
    context ={
        "form": RegistrationForm
    }
    return render(request, "register.html", context)

def add_user(request):
    # getting form data through post request
    form = RegistrationForm(request.POST)
    if form.is_valid():
        # creating object and passing form values
        register_user = RegistrationData(username= form.cleaned_data['username'],
                                    password= form.cleaned_data['password'],
                                    email = form.cleaned_data['email'],
                                    phone= form.cleaned_data['phone']
                                    )
        register_user.save()
        # flash messages in django here displaying in register.html
        messages.add_message(request, messages.SUCCESS, "You have registered successfully") 
        print(messages)
#    will be redirected to register page i,e, given the name of url 
    return redirect('register')

def modelform(request):
    context = {
        "modelform": RegistrationModel
    }

    return render(request, "modelform.html", context)