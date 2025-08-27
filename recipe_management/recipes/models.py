from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length=200, blank=True)


    def __str__(self):
         return f"{self.quantity} {self.unit} {self.ingredient.name} for {self.recipe.title}"
