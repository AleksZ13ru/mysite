from django import forms
from .models import Event, Memo, Note


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'day_create', 'comment')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['day_create'].widget.attrs.update({'class': 'span2', 'id': 'dp_event'})
        self.fields['title'].widget.attrs.update({'placeholder': 'Событие'})
        self.fields['comment'].widget.attrs.update({'placeholder': 'Комментарий'})


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'day_create', 'comment')

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['day_create'].widget.attrs.update({'class': 'span2', 'id': 'dp_memo'})
        self.fields['title'].widget.attrs.update({'placeholder': 'Заметка'})
        self.fields['comment'].widget.attrs.update({'placeholder': 'Комментарий'})


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('number', 'title', 'to_whom', 'day_create', 'text')
