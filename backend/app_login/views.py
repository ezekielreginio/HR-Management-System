from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from . import forms
# Create your views here.

def index(request):
    login_form = forms.Login
    if request.method == "POST":
        login_form = forms.Login(request.POST)
        
        if login_form.is_valid():
            user = authenticate(request, username=request.POST.get("login"), password=request.POST.get("password"))
            login(request, user)
            return redirect("dashboard/")
    
    context = {'login_form':login_form}
    return render(request, "./index.html", context)