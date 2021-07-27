from django.contrib import admin
from .models import Post, Comment

# admin for blogs.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'body',
        'intro',
    )

    read_only = ('slug',)


admin.site.register(Comment)
