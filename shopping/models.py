from django.db import models
from django.conf import settings

class ShoppingList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, blank=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item} ({'✓' if self.is_checked else '✗'})"


# Create your models here.
