from django.shortcuts import render, redirect
from .models import *
from .forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/users/register')
    else:
        return render(request, 'register.html', {'form':form})