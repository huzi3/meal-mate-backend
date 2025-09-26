import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1"

def search_recipes(query):
    """Search recipes by name."""
    r = requests.get(f"{BASE_URL}/search.php", params={"s": query})
    r.raise_for_status()
    data = r.json()
    return data.get("meals", [])  # TheMealDB returns {'meals': [...]}

def get_recipe_by_id(meal_id):
    """Get a single recipe by ID."""
    r = requests.get(f"{BASE_URL}/lookup.php", params={"i": meal_id})
    r.raise_for_status()
    data = r.json()
    return data.get("meals", [])[0] if data.get("meals") else None
