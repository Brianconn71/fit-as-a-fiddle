from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#Discount Model
class Discount(models.Model):
    code = models.CharField(max_length=25, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_rate = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code
