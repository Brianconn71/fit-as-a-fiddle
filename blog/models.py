from django.db import models
from django.contrib.auth.models import User


# blog model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    intro = models.TextField(max_length=250, null=False, blank=False)
    body = models.TextField(max_length=1000, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-date_added']

