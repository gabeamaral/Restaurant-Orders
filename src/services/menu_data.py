from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for meal in reader:
                meal_name = meal['dish']
                meal_price = float(meal['price'])
                meal_ingredients = meal['ingredient']
                meal_amount = int(meal['recipe_amount'])

                self.dishes.add(Dish(
                    meal_name,
                    meal_price,
                    ))
                prox_meal = next(iter(self.dishes))

                prox_meal.add_ingredient_dependency(
                    Ingredient(meal_ingredients), meal_amount,
                )
