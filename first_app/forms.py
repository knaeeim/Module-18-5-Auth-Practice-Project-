from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

# Create your models here.

class RegistrationForms(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        # fields = "__all__"

class changeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', "first_name", "last_name"]