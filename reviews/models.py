from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Review system model
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=254, null=False, blank=False)
    comment = models.TextField(max_length=1000, null=False, blank=False)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1, null=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
