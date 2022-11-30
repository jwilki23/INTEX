from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import CreateUserForm
from .models import Person, Stage, Morbidity
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
    success_url = '/login2'

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

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mydata')
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'trackme/login.html', context)

def signupPageView(request) : 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            person = Person()
            form_user = form.cleaned_data.get('username')

            person.first_name = request.POST['first_name']
            person.last_name = request.POST['last_name']
            person.age = request.POST['age']
            person.gender = request.POST['gender']
            person.weight = request.POST['weight']
            person.height_feet = request.POST['height_feet']
            person.height_inches = request.POST['height_inches']
            person.user_name = request.POST.get('username')
            person.password = 'test'
            # user.stage = request.POST['stage']

            stage_id = request.POST['stage']
            assign_stage = Stage.objects.get(id=stage_id)
            person.stage = assign_stage
            # person.morbidity_type = request.POST['morbidity_type', False]

            person.save()
            messages.success(request, 'Account was created for ' + form_user)
            return redirect('login')
    else:
        form = UserCreationForm()
        stage = Stage.objects.all()
        morbidity = Morbidity.objects.all()

        context = {
            'form': form,
            'stage' : stage,
            'morbidity': morbidity
        }
        return render(request, 'trackme/signup.html', context)

        
def journalPageView(request) :
    return render(request, 'trackme/journal.html')

