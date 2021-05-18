from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.


def registration(request):
    form=CreateUserForm()

    if request.method=="POST":
    	form = CreateUserForm(request.POST)
    	if form.is_valid():
    		form.save()
    		messages.success(request,'Account has created sucesfully')
    		return redirect('login')

    context = {'form':form}
    return render(request, 'registration.html', context)

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			auth_login(request,user)
			return redirect('index')

    
	return render(request, 'login.html')