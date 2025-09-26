from rest_framework.routers import DefaultRouter
from .views import MealPlanViewSet, ShoppingListItemViewSet

router = DefaultRouter()
router.register(r'mealplans', MealPlanViewSet, basename='mealplan')
router.register('shopping-items', ShoppingListItemViewSet, basename='shopping-items')

urlpatterns = router.urls
