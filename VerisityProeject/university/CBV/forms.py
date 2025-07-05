from django import forms
from . import models

class FriendsFrom(forms.ModelForm):
  class Meta:
    model=models.friends
    fields=['first_name', 'last_name', 'home', 'email']