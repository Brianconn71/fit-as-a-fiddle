from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Review system model
class Review(models.Model):
    RATING_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=254, null=False, blank=False)
    comment = models.TextField(max_length=1000, null=False, blank=False)
    rating = models.IntegerField(choices=RATING_CHOICES, null=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
