from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# blog model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField()
    intro = models.TextField(max_length=250, null=False, blank=False)
    body = models.TextField(max_length=1000, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta: 
        ordering = ['-date_added']

