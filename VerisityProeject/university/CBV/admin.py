from django.contrib import admin
from . models import Friends

# Register your models here.
@admin.register(Friends)
class friendAdmin(admin.ModelAdmin):
   list_display = ('id', 'first_name', 'last_name', 'home', 'email')