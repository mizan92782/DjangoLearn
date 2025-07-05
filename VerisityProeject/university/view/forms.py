

from django import forms
from .models import Views


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Views
        fields = ['title', 'description']  
