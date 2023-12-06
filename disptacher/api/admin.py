from django.contrib import admin
from .models import Client, Dispatch, Message


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'phone',
        'operator',
        'tag',
        'timezone'
    )


class DispatchAdmin(admin.ModelAdmin):
    list_display = (
        'dispatch_date',
        'text',
        'client_filter',
        'dispatch_date_end'
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'send_date',
        'dispatch_status',
        'client_id',
        'dispatch'
    )


admin.site.register(Client, ClientAdmin)
admin.site.register(Dispatch, DispatchAdmin)
admin.site.register(Message, MessageAdmin)
