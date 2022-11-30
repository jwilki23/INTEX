from django.shortcuts import render
from django.http import HttpResponse
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
    data = JournalEntry.objects.all()

    context = {
        'journalentry' : data
    }
    return render(request, 'trackme/mydata.html', context)

def loginPageView(request) : 
    return render(request, 'trackme/login.html')

def signupPageView(request) : 
    return render(request, 'trackme/signup.html')

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
        
        journalentry = JournalEntry()

        # journalentry_id = request.POST['journalentry_id']

        # journalentry = JournalEntry.objects.get(id=journalentry_id)
    
        journalentry.date = request.POST['date']
        journalentry.meal = request.POST['meal']
        journalentry.food_name = request.POST['food_name']
        journalentry.servings = request.POST['servings']

        journalentry.save()
        return myDataPageView(request)

    else:
        return render(request, 'trackme/addJournalEntry.html')



def deleteEntryPageView(request,journalentry_id) :
    data = JournalEntry.objects.get(id = journalentry_id)

    data.delete()

    return myDataPageView(request)