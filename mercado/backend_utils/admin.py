from django.contrib import admin
from .models import ActionLog

@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'object_repr')
    list_filter = ('action', 'timestamp', 'user')
    readonly_fields = ('timestamp',)
    search_fields = ('object_repr',)
