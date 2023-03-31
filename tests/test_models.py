from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test1",
        )
        self.assertEqual(str(dish_type), str(dish_type.name))

    def test_dish_str(self):
        dish = Dish.objects.create(
            name="test1",
            price=5
        )
        self.assertEqual(str(dish), str(dish.name))

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="test12",
            last_name="test2",
            years_of_experience=1,
        )
        self.assertEqual(
            str(cook), f"{cook.username} ({cook.first_name} {cook.last_name})"
        )
