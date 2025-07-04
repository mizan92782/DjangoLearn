import django.contrib.auth.forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class DefineUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username',  'first_name', 'last_name','email', 'password1', 'password2',)




# modify user change form
class UserChangeScreenModify(UserChangeForm):
  password=None
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')