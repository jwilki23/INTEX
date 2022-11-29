from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

from django.shortcuts import redirect
# Create your views here.

class SignupView(CreateView) :
    form_class = SignUpForm
    template_name = 'trackme/register.html'
    success_url = '/mydata'

    def get(self, request, *args, **kwargs) :
        if self.request.user.is_authenticated :
            return redirect('/mydata')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView) :
    template_name = 'trackme/logout.html'
class LoginInterfaceView(LoginView) :
    template_name = 'trackme/login2.html'

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