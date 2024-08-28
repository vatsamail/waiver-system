from django import forms
from .models import Waiver

class WaiverForm(forms.ModelForm):
    class Meta:
        model = Waiver
        fields = ['type', 'project', 'domain', 'module', 'error_code', 'description']
