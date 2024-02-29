from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_time', 'modified_time')
    list_display_links = ('id', 'content')
    list_filter = ('created_time', 'modified_time')
    search_fields = ('content',)
    date_hierarchy = 'created_time'