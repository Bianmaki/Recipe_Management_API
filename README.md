**RECIPE_MANAGEMENT_API**
A Django + Django REST Framework (DRF) project for managing recipes, ingredients, categories, and users.  
This API supports CRUD operations, authentication, and filtering recipes by category or ingredient.  
It simulates a real-world recipe management system with a focus on backend development.

**FEATURES**
- **User Management (CRUD)**
  - Register, view, update, and delete users
  - Unique username, email, and password
  - Authenticated users can create and manage their own recipes

- **Recipe Management (CRUD)**
  - Create, view, update, and delete recipes
  - Recipe attributes: Title, Description, Ingredients, Instructions, Category, Preparation Time, Cooking Time, Servings, Created Date
  - Each recipe is linked to its creator (user)

- **Ingredient Management (CRUD)**
  - Create, view, update, and delete ingredients
  - Ingredients can be linked to recipes via `RecipeIngredient` (with quantity, unit, and notes)

- **Category Management (CRUD)**
  - Create, view, update, and delete categories
  - Recipes can be grouped by category

- **Search and Filter**
  - View recipes by category
  - View recipes by ingredient
  - Search recipes by title, category, ingredient, or preparation time (to be extended)
**The payloads I used**
  *Users*
   {
  "username": "Lisathecook",
  "email": "lisaagness02@gmail.com",
  "password": "Metting123"
}


  {
  "username": "Lisathecook",
  "email": "lisaagness02@gmail.com",
  "password": "Metting123"
}
*ingredients*

{
    "name": "flour",
    "description": "wheat flour"
}

{
    "name": "milk",
    "description": "powdered milk"
}

{
"title": "Bread",
  "description": "White Bread.",
  "instructions": "Mix ingredients, bake at 180°C for 30 minutes.",
  "category": 1,
  "prep_time": 20,
  "cook_time": 30,
  "servings": 8
}

  
**FEATURES ADDED**
-**Authentication**
-Implemented Django Rest Framework's TokenAuthentication
Users can log in to receive an authentication Token.
Use the token to authenticate requests.

- **Sorting**
Recipes can be ordered by:
- created_at
- prep_time
- cook_time

-**Pagination**
Implemented pagination using **PageNumberPagination*
Default page size is 10 recipes per page.




