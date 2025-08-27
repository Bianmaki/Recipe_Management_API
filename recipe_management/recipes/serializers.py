from rest_framework import serializers
from .models import Recipe, Ingredient, Category, RecipeIngredient, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ["id", "ingredient", "quantity", "unit", "notes"]


class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    ingredients = RecipeIngredientSerializer(
        source="recipeingredient_set", many=True, read_only=True
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "user",
            "title",
            "description",
            "instructions",
            "category",
            "prep_time",
            "cook_time",
            "servings",
            "created_at",
            "ingredients",
        ]
