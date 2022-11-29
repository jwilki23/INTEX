from django.urls import path
from .views import indexPageView
from .views import myDataPageView
from .views import loginPageView
from .views import signupPageView


urlpatterns = [
    path("", indexPageView, name="index"),
    path("mydata/", myDataPageView, name="mydata"),
    path("login/", loginPageView, name='login'),
    path("signup/", signupPageView, name='signup'),
]
