from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_on_host', 'created_at')
    list_filter = ('created_on_host', 'created_at')
    search_fields = ('text', 'author')

