# mealplans/models.py
from django.db import models
from django.conf import settings
from recipes.models import Recipe

class MealPlan(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.recipe.title}"


class ShoppingListItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shopping_items'
    )
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, blank=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({'✔' if self.checked else '✗'})"

# Create your models here.
