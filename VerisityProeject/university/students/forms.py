from django import forms
from .models import Student


#from from input data
class StudentForm(forms.ModelForm):
  #meta defines this model connected with which model and which fields 
  # this model work for decleared model
  class Meta:
    model=Student
    #this model take dat for this fields
    fields = ['first_name', 'last_name', 'batch']
    
    
  #clearn data under a condition
  def clean_first_name(self):
      first_name_validation = self.cleaned_data.get('first_name')
      
      if len(first_name_validation) < 3:
          
          raise forms.ValidationError("First name must be at least 3 characters long.")
  
  
        # TODO Validation
  
      return first_name_validation

