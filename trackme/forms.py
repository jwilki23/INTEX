from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = '__all__'

class SignUpForm(UserCreationForm) :
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    morbidity_type = forms.CharField(max_length=30)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10)
    weight = forms.DecimalField(max_digits=8, decimal_places=2)
    height_feet = forms.IntegerField()
    height_inches = forms.IntegerField()
    stage = forms.CharField(max_length=20)

    class meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'morbidity_type', 'age', 'gender', 'weight', 'height_feet', '/n'
        'height_inches', 'stage', 'password1', 'password2')
  