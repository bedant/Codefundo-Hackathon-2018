from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254,required=False, help_text='Optional. Inform a valid email address.')
    Phone_number  = forms.IntegerField(required=True , help_text='Required.')
    city = forms.CharField(max_length=30, required=True, help_text='Required.')
    state = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','Phone_number','city','state', 'password1', 'password2', )