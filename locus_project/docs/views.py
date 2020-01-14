from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created')
            return redirect('')
    else:
        form = UserRegisterForm()
    return render(request, 'docs/login.html',)

def index(request):
    return render(request, 'docs/index.html')
