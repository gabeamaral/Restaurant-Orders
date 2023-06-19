from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        meals = {}

        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for meal in reader:
                meal_key = meal["ingredient"]
                meal_ingredients = Ingredient(meal_key)
                self.dishes.add(meal_ingredients)
                meal_name = meal["dish"]
                meal_price = float(meal["price"])
                meal_atributes = meals.get(meal_name)

                if meal_atributes is None:
                    meal_atributes = Dish(meal_name, meal_price)
                    meals[meal_name] = meal_atributes
                meal_amount = int(meal["recipe_amount"])
                meal_atributes.add_ingredient_dependency(
                    meal_ingredients,
                    meal_amount,
                    )

        self.dishes = set(meals.values())
