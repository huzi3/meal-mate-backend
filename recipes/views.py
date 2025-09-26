from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Favorite, Recipe
from .serializers import FavoriteSerializer
from .services import search_recipes, get_recipe_by_id

@api_view(['GET'])
def recipe_list(request):
    query = request.GET.get('q', 'chicken')  # default search
    meals = search_recipes(query)
    # reshape for frontend (clean minimal JSON)
    results = []
    for m in meals:
        results.append({
            "id": m["idMeal"],
            "title": m["strMeal"],
            "category": m.get("strCategory"),
            "area": m.get("strArea"),
            "thumbnail": m.get("strMealThumb"),
        })
    return Response(results)

@api_view(['GET'])
def recipe_detail(request, id):
    meal = get_recipe_by_id(id)
    if not meal:
        return Response({"error": "Not found"}, status=404)
    data = {
        "id": meal["idMeal"],
        "title": meal["strMeal"],
        "category": meal["strCategory"],
        "area": meal["strArea"],
        "instructions": meal["strInstructions"],
        "ingredients": [
            {
                "ingredient": meal[f"strIngredient{i}"],
                "measure": meal[f"strMeasure{i}"]
            }
            for i in range(1, 21)
            if meal.get(f"strIngredient{i}")
        ],
        "image": meal["strMealThumb"]
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite_list(request):
    favs = Favorite.objects.filter(user=request.user)
    return Response(FavoriteSerializer(favs, many=True).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    external_id = request.data.get('external_id')
    title = request.data.get('title')
    image_url = request.data.get('image_url', '')

    if not external_id or not title:
        return Response({"error": "Missing data"}, status=400)

    recipe, _ = Recipe.objects.get_or_create(
        external_id=external_id,
        defaults={'title': title, 'image_url': image_url}
    )
    Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    return Response({"message": "Added to favorites"}, status=201)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_favorite(request, recipe_id):
    try:
        recipe = Recipe.objects.get(external_id=recipe_id)
        fav = Favorite.objects.get(user=request.user, recipe=recipe)
        fav.delete()
        return Response({"message": "Removed from favorites"}, status=204)
    except (Recipe.DoesNotExist, Favorite.DoesNotExist):
        return Response({"error": "Not found"}, status=404)
# Create your views here.
