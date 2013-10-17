from django.contrib import admin
from models import *

class EnrollAdmin(admin.ModelAdmin):
    list_display = ('reg_code', 'will_come', 'add_date', 'conference')
    list_filter = ['conference', 'add_date', 'will_come']
    search_fields = ['reg_code']
    
admin.site.register(Enroll, EnrollAdmin)