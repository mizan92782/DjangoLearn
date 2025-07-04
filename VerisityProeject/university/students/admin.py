from django.contrib import admin
import django.db
from .models import Student


#admin model view
#!without this, the admin interface won't display the model in table
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'batch')
    
    
# Register your models here.
admin.site.register(Student, StudentAdmin)  # Assuming 'Student' is the model you want to register