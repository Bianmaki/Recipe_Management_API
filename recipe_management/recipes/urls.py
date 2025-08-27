from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, CategoryViewSet, UserViewSet, IngredientViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r"ingredients", IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),  # For login/logout
]