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
from trackme.models import JournalEntry

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
    #retrieve current person based on logged in username
    current_user = request.user.username
    current_person = Person.objects.get(user_name = current_user)

    non_users = Person.objects.exclude(id=current_person.id)
    unordered_data = JournalEntry.objects.exclude(person_id__in=non_users)
    data = unordered_data.order_by('date')

    data1 = JournalEntry.objects.all()
    context = {
        'data': data1,
    }

    morbidities = current_person.morbidity_type.all()

    context = {
        'current_person' : current_person,
        'journalentry' : data,
        'morbidities' : morbidities
    }
    return render(request, 'trackme/mydata.html', context)

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

            person.first_name = request.POST['first_name'].title()
            person.last_name = request.POST['last_name'].title()
            person.age = request.POST['age']
            person.gender = request.POST['gender']
            person.weight = request.POST['weight']
            person.height_feet = request.POST['height_feet']
            person.height_inches = request.POST['height_inches']
            person.user_name = request.POST.get('username')
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

        

# def addJournalEntryPageView(request) :
#     return render(request, 'trackme/addJournalEntry.html')

def showSingleEntryPageView(request, journalentry_id) :
    data = JournalEntry.objects.get(id = journalentry_id)

    context = {
        "record" : data,
    }
    return render(request, 'trackme/updatejournalentry.html' , context)

# def showMainEntryPageView(request, journalentry_id) :
#     data = JournalEntry.objects.get(id = journalentry_id)

#     context = {
#         "record" : data,
#     }
#     return render(request, 'trackme/addJournalEntry.html' , context)

def updateJournalEntryPageView (request) :
    if request.method == 'POST' :
        journalentry_id = request.POST['journalentry_id']

        journalentry = JournalEntry.objects.get(id=journalentry_id)
    
        journalentry.date = request.POST['date']
        journalentry.meal = request.POST['meal']
        journalentry.food_name = request.POST['food_name']
        journalentry.servings = request.POST['servings']
        # journalentry.person = request.POST['person']

        journalentry.save()
    return myDataPageView(request)


def addJournalEntryPageView (request) :
    if request.method == 'POST' :
        
        current_user_name = request.user.username
        journalentry = JournalEntry()

        # journalentry_id = request.POST['journalentry_id']

        # journalentry = JournalEntry.objects.get(id=journalentry_id)
    
        journalentry.date = request.POST['date']
        journalentry.meal = request.POST['meal']
        journalentry.food_name = request.POST['food_name'].title()
        journalentry.servings = request.POST['servings']
        journalentry.person = Person.objects.get(user_name = current_user_name)

        journalentry.save()
        return myDataPageView(request)

    else:
        return render(request, 'trackme/addJournalEntry.html')



def deleteEntryPageView(request,journalentry_id) :
    data = JournalEntry.objects.get(id = journalentry_id)

    data.delete()

    return myDataPageView(request)

def addMorbidEntryPageView (request) :
    current_person = Person.objects.get(user_name = request.user.username)
    morbidities = current_person.morbidity_type.all()

    avail_morb = Morbidity.objects.exclude(id__in=morbidities)

    context = {
        'avail' : avail_morb,
        'morbidities' : morbidities
    }

    return render(request, 'trackme/addMorbidEntry.html', context)

def addNewMorbidityPageView(request) :
    if request.method == 'POST' :
        current_person = Person.objects.get(user_name = request.user.username)

        morb = request.POST['new_morb']
        current_person.morbidity_type.add(Morbidity.objects.get(id=morb))

    return myDataPageView(request)




