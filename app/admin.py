from django.contrib import admin
from app.models import Location, Message


class LocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
    search_fields = ('user', 'location')
    readonly_fields = ['user', 'location','date']
    list_filter = ('location',)


class MessageAdmin(admin.ModelAdmin):
    search_fields = ('user', 'email')
    readonly_fields = ['user', 'email', 'message','date']
    list_display = ('user', 'email', 'message')
    list_filter = ('user', 'email',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.index_title = "Checkin-checkout"
admin.site.site_title = "Checkin-checkout"
admin.site.site_header = "Admin"
