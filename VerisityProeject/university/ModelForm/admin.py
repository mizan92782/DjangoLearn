from django.contrib import admin
from .models import People


# Register your models here.
@admin.register(People)
class StudentsAdmin(admin.ModelAdmin):
    class Meta:
        model = People
        list_display = ('name', 'age', 'address')