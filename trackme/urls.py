from django.urls import path
from .views import indexPageView
from .views import myDataPageView
from .views import loginPageView
from .views import signupPageView
from .views import LoginInterfaceView
from .views import LogoutInterfaceView
from .views import SignupView
from .views import showSingleEntryPageView
from .views import updateJournalEntryPageView
from .views import deleteEntryPageView
from .views import addJournalEntryPageView
from .views import addMorbidEntryPageView
from .views import addNewMorbidityPageView
# from .views import showMainEntryPageView



urlpatterns = [
    path("mydata/", myDataPageView, name="mydata"),
    path("login/", loginPageView, name='login'),
    path("signup/", signupPageView, name='signup'),
    path("addJournalEntry/", addJournalEntryPageView, name="addJournalEntry"),
    path('login2/', LoginInterfaceView.as_view(), name='login2' ),
    path('logout/', LogoutInterfaceView.as_view(), name='logout' ),
    path('signup2/', SignupView.as_view(), name='signup2' ),
    path('showentries/<int:journalentry_id>/', showSingleEntryPageView, name='showSingleEntry'),
    # path('showentry/<int:journalentry_id>/', showMainEntryPageView, name='showMainEntry'),
    path('updateJournalEntry/', updateJournalEntryPageView, name='updateJournal'),
    path('deleteentry/<int:journalentry_id>/', deleteEntryPageView, name='deleteEntry'),
    path("addMorbidEntry/", addMorbidEntryPageView, name="addMorbidEntry"),
    path("addNewMorbidity/", addNewMorbidityPageView, name="addNewMorbidity"),
    path("", indexPageView, name="index"),
]
