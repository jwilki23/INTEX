from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'trackme/signup.html')
def journalPageView(request) :
    return render(request, 'trackme/journal.html')