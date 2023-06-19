from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    sushi = Dish("sushi", 62.99)
    sashimi = Dish("sashimi", 42.99)

    assert sushi.name == "sushi"

    assert sushi == sushi
    assert sushi != sashimi

    assert repr(sushi) == "Dish('sushi', R$62.99)"

    assert hash(sushi) == hash(sushi)
    assert hash(sushi) != hash(sashimi)

    sushi.add_ingredient_dependency(Ingredient("arroz"), 0.5)
    sushi.add_ingredient_dependency(Ingredient("peixe"), 0.3)
    sushi.add_ingredient_dependency(Ingredient("alga"), 0.1)

    assert sushi.get_ingredients() == set([
        Ingredient("arroz"),
        Ingredient("peixe"),
        Ingredient("alga"),
    ])

    assert sushi.get_restrictions() == set('')

    with pytest.raises(ValueError):
        Dish('sushi', -1)
    with pytest.raises(TypeError):
        Dish('sushi', 'R$62.99')
