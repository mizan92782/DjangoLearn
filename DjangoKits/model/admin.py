from django.contrib import admin
from .models import Mans, Students, Womens, Couples

@admin.register(Students)
# Student Admin
class StuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'batch','group')

@admin.register(Mans)
# Mans Admin
class MansAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'batch')


@admin.register(Womens)
#Womens Admin
class WomensAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'batch')


@admin.register(Couples)
# Couples Admin
class CouplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'husband', 'wife', 'husband_age', 'wife_age', 'husband_batch', 'wife_batch')
