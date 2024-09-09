from django.contrib import admin
from .models import blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updated_at')  # Customize list view
    search_fields = ('user__username', 'text')  # Add search functionality

admin.site.register(blog, BlogAdmin)
