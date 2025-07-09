from django.contrib import admin
import django.db
from .models import Students

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'email')
    
   