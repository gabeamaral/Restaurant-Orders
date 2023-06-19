from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("presunto")
    assert presunto.name == "presunto"
    assert presunto.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert str(presunto) == "Ingredient('presunto')"

    ingredient_1 = Ingredient("presunto")
    ingredient_2 = Ingredient("presunto")
    ingredient_3 = Ingredient("queijo mussarela")

    assert ingredient_1 == ingredient_2
    assert ingredient_1 != ingredient_3

    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)
