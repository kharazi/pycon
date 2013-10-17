from django.contrib import admin

from models import *

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'reg_start', 'reg_quota')

class TalkAdmin(admin.ModelAdmin):
    list_display = ('user','conference','title', 'description', 'short_abstract','status','submit_date')
    list_filter = ['status']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):  
    pass
        
        
class TalkAttachmentAdmin(admin.ModelAdmin):    
    list_display =('talk','attachment', 'accepted','name', 'about')
        

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Talk , TalkAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TalkAttachment,TalkAttachmentAdmin)