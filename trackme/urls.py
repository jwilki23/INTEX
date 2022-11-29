from django.urls import path
from .views import indexPageView
from .views import myDataPageView
from .views import loginPageView
from .views import signupPageView
from .views import journalPageView
from .views import LoginInterfaceView
from .views import LogoutInterfaceView
from .views import SignupView


urlpatterns = [
    path("", indexPageView, name="index"),
    path("mydata/", myDataPageView, name="mydata"),
    path("login/", loginPageView, name='login'),
    path("signup/", signupPageView, name='signup'),
    path("journal/", journalPageView, name="journal"),
    path('login2/', LoginInterfaceView.as_view(), name='login2' ),
    path('logout/', LogoutInterfaceView.as_view(), name='logout' ),
    path('signup2/', SignupView.as_view(), name='signup2' ),
]
