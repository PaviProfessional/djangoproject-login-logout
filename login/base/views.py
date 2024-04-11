from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  # for form creation
from . forms import UserRegisterForm
from django.contrib import messages     #for give a successfull message


# Create your views here.
def home(request):
    return render(request,"base/home.html")

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()    #save in database
            username=form.cleaned_data.get("username")
            messages.success(request,f'Hi {username}, Your account was Created Successfully!')
            return redirect("home")
    else:
        form=UserRegisterForm()       
    return render(request,"base/register.html",{"form":form})   
    
     
def thanks(request):
    return render(request,"base/thanks.html")
 