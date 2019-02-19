from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Write the content here'}
        ),
        max_length=5000,
        help_text='The max length of the text is 5000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']