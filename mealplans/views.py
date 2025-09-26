from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MealPlan, ShoppingListItem
from .serializers import MealPlanSerializer, ShoppingListItemSerializer

class MealPlanViewSet(viewsets.ModelViewSet):
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ShoppingListItemViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingListItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShoppingListItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # toggle checked/unchecked
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        item = self.get_object()
        item.checked = not item.checked
        item.save()
        return Response({'checked': item.checked})

# Create your views here.
