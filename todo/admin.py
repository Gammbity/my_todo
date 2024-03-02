from django.contrib import admin
from .models import TodoModel

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'todo', 'created_at']
    list_display_links = ['id', 'todo', 'created_at']