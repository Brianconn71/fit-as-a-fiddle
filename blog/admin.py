from django.contrib import admin
from .models import Post, Comment

# admin for blogs.
admin.site.register(Post)
admin.site.register(Comment)
