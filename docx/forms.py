from django import forms
from .models import Event, Memo


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'day_create', 'comment')


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('number', 'title', 'to_whom', 'day_create', 'text')
