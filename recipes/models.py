from django.db import models
from django.conf import settings

class Recipe(models.Model):
    # if caching recipes from an external API
    external_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)
    summary = models.TextField(blank=True)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.username} -> {self.recipe.title}"
