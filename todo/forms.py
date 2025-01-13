from django import forms
from .models import Todo
from django.forms.widgets import DateTimeInput

class TodoForm(forms.ModelForm):
    date = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Todo
        fields = "__all__"