from django.shortcuts import render


from . import forms
# Create your views here.
def index(request):
    login_form = forms.Login
    context = {'login_form':login_form}
    return render(request, "./index.html", context)