from django import forms
from beckett.apps.sites.models import Chronology
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField


class ChronologyForm(forms.ModelForm):
    class Meta:
        model = Chronology
        fields = '__all__'
        widgets = {
            'description': forms.HTMLField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        }