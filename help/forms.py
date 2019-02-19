from django import forms
from .models import Ticket
class TicketForms(forms.ModelForm):
    #name = forms.CharField(max_length=120,required=True,help_text='Enter your name')
    #phone_number = forms.CharField(min_length=10,max_length=10,help_text='Enter your phone number')
    #comment = forms.CharField(required=True, widget=forms.Textarea,help_text='How can we help you?',max_length=1000)

    class Meta:
        model = Ticket
        fields = ['name','phone_number','subject','description']