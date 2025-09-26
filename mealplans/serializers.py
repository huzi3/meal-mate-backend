from rest_framework import serializers
from .models import MealPlan, ShoppingListItem
from recipes.models import Recipe

class MealPlanSerializer(serializers.ModelSerializer):
    recipe_title = serializers.ReadOnlyField(source='recipe.title')

    class Meta:
        model = MealPlan
        fields = ['id', 'date', 'meal_type', 'recipe', 'recipe_title']


class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ['id', 'name', 'quantity', 'checked']

