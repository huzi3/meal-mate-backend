from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('<str:id>/', views.recipe_detail, name='recipe_detail'),

    # Favorites
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('favorites/add/', views.add_favorite, name='add_favorite'),
    path('favorites/remove/<str:recipe_id>/', views.remove_favorite, name='remove_favorite'),
]
