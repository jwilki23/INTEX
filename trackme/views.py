from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import Person


# Create your views here.

# def indexPageView(request) :
#     return HttpResponse('Welcome to the index page')

def indexPageView(request) :
    return render(request, 'trackme/index.html')

def myDataPageView(request) :
    return render(request, 'trackme/mydata.html')

def loginPageView(request) : 
    return render(request, 'trackme/login.html')

def signupPageView(request) : 
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            user = Person()

            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.age = request.POST['age']
            user.gender = request.POST['gender']
            user.weight = request.POST['weight']
            user.height_feet = request.POST['height_feet']
            user.height_inches = request.POST['height_inches']

            user.save()
    
    context = {
        'form': form,
    }
    return render(request, 'trackme/signup.html', context)

