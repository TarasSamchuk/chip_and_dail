from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def user_page(request):
    return render(request, 'chipdail/home_page.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'profiles/registration.html', context={'form': form})

def user_detail(request):
    return render(request, 'profiles/user_detail.html', context={'user': request.user})






