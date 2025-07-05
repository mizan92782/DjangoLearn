from django.contrib import admin
from .models import Views

# Register your models here.
@admin.register(Views)
class viewsAdmin(admin.ModelAdmin):
  list_display = ('view_id', 'title', 'description', 'time')
  
  

