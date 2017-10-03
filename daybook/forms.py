from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        widgets = {
            'defect': forms.Textarea(attrs={'rows': 10}),
            'working': forms.Textarea(attrs={'rows': 10}),
        }
        fields = ('equipment', 'defect', 'working')
