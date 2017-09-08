from django import forms
from .models import Event, Memo, Note


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Событие'}),
            'day_create': forms.TextInput(attrs={'class': 'span2', 'id': 'dp_event'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Комментарий'})
        }
        fields = ('title', 'day_create', 'comment')

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['day_create'].widget.attrs.update({'class': 'span2', 'id': 'dp_event'})
    #     self.fields['title'].widget.attrs.update({'placeholder': 'Событие'})
    #     self.fields['comment'].widget.attrs.update({'placeholder': 'Комментарий'})


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заметка'}),
            'day_create': forms.TextInput(attrs={'class': 'span2', 'id': 'dp_memo'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Комментарий'})
        }
        fields = ('title', 'day_create', 'comment')

    # def __init__(self, *args, **kwargs):
    #     super(NoteForm, self).__init__(*args, **kwargs)
    #     self.fields['day_create'].widget.attrs.update({'class': 'span2', 'id': 'dp_memo'})
    #     self.fields['title'].widget.attrs.update({'placeholder': 'Заметка'})
    #     self.fields['comment'].widget.attrs.update({'placeholder': 'Комментарий'})


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10}),
            'day_create': forms.TextInput(attrs={'class': 'span2', 'id': 'dp_memo'})
        }
        fields = ('number', 'title', 'to_whom', 'day_create', 'text', 'who')

    # def __init__(self, *args, **kwargs):
    #     super(MemoForm, self).__init__(*args, **kwargs)
        # self.fields['day_create'].widget.attrs.update({'class': 'span2', 'id': 'dp_memo'})
        # self.fields['text'].widget(forms.Textarea)
