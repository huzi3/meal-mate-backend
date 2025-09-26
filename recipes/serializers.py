from rest_framework import serializers
from .models import Favorite, Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'external_id', 'title', 'image_url']

class FavoriteSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'recipe', 'added_at']
