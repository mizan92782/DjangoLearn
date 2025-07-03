
# Register your models here.
from payments.models import Name  
from django.contrib import admin


# show the model in admin panel in table
class NameAdmin(admin.ModelAdmin):
    list_display = ('id','pai_id', 'pay_option', 'min_pay')
    search_fields = ('pay_option',)

admin.site.register(Name, NameAdmin)
