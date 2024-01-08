from django import forms
from .models import Topic, Entry

# Form for adding topics
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {
            'text': 'Topic'
        }
        widget = {
            'text': forms.TextInput(attrs={
                'class': 'form-input',
                'id': 'topic-input',
                'placeholder': 'New topic name...'
            })
        }

# Form for adding entries
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {
            'text': 'Entry'
        }
        widget = {
            'text': forms.TextInput(attrs={
                'class': 'form-input',
                'id': 'entry-input',
                'placeholder': 'New entry text...'
            })
        }
