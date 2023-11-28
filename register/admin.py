from django.contrib import admin
from .models import Invitee, Registration, Memento

class InviteeAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'designation', 'project', 'invited', 'spot_registered', 'pm_dept', 'vendor')
    list_filter = ('invited', 'spot_registered', 'pm_dept', 'vendor')
    search_fields = ('email', 'first_name', 'last_name')    

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('invitee', 'registration_date', 'arrival_date', 'departure_date', 'arrival_at_venue')
    list_filter = ('registration_date', 'arrival_date', 'departure_date')
    search_fields = ('invitee__email', 'invitee__first_name', 'invitee__last_name')

class MementoAdmin(admin.ModelAdmin):
    list_display = ('registration', 'tag_generated', 'tag_printed', 'tag_collected', 'issued_to', 'issued_by')
    list_filter = ('tag_generated', 'tag_printed', 'tag_collected')
    search_fields = ('registration__invitee__email', 'registration__invitee__first_name', 'registration__invitee__last_name')

admin.site.register(Invitee, InviteeAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Memento, MementoAdmin)

admin.site.site_header = "PM23"
admin.site.site_title = "PM23 Admin Portal"