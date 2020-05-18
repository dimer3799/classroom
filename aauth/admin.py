from django.contrib import admin
from .models import Post

# Register your models here.

class Aadmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'published')

admin.site.register(Post, Aadmin)