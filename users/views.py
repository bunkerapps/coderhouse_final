from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .forms import UserRegisterForm
from django.views.decorators.http import require_POST



# Create your views here.
def login(request):
    ...
    context={"title":'Login'}
    return render(request, 'login.html',context)

@require_POST
def logout(request):
    auth_logout(request)
    context = {"title": 'Logout'}
    return render(request, 'registration/logout.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

    
def about(request):
    context = {"title": 'About Us'}
    return render(request, 'about.html', context)