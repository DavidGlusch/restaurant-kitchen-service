from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType, Cook

DISH_TYPE_CREATE_URL = reverse("kitchen:dish-type-create")
DISH_TYPE_URL = reverse("kitchen:dish-type-list")
DISH_URL = reverse("kitchen:dish-list")
DISH_CREATE_URL = reverse("kitchen:dish-create")
COOK_URL = reverse("kitchen:cook-list")
COOK_CREATE_URL = reverse("kitchen:cook-create")


class PublicDishTypeTest(TestCase):
    def test_dish_type_login_required(self):
        response = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(response, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test1234567",
        )
        self.client.force_login(self.user)

    def test_dish_type_create(self):
        data = {"name": "test"}
        response = self.client.post(DISH_TYPE_CREATE_URL, data=data)
        dish_type = DishType.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(DishType.objects.count(), 1)
        self.assertEqual(dish_type.name, "test")

    def test_dish_type_retrieve(self):
        DishType.objects.create(name="test1")
        DishType.objects.create(name="test2")

        response = self.client.get(DISH_TYPE_URL)
        dish_type = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_type_list"]),
                         list(dish_type))
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")


class PublicDishTests(TestCase):
    def test_dish_login_required(self):
        response = self.client.get(DISH_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test2",
        )
        self.client.force_login(self.user)

    def test_dish_create(self):
        dish_type = DishType.objects.create(
            name="test2",
        )
        cook = Cook.objects.create(
            username="user",
            password="test1",
            years_of_experience=5
        )

        data = {
            "name": "test1",
            "price": 1,
            "description": "test",
            "dish_type": dish_type.pk,
            "cooks": [cook.pk]
        }
        response = self.client.post(DISH_CREATE_URL, data=data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dish.objects.count(), 1)
        self.assertEqual(Dish.objects.first().name, "test1")

    def test_dish_retrieve(self):
        dish_type = DishType.objects.create(
            name="test3",
        )
        Dish.objects.create(name="test1", price=5.1, dish_type=dish_type)
        Dish.objects.create(name="test2", price=5.1, dish_type=dish_type)

        dishes = Dish.objects.all()
        response = self.client.get(DISH_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test2",
            password="test2",
        )
        self.client.force_login(self.user)

    def test_cook_create(self):
        data = {
            "username": "test",
            "password1": "qweqwsadfasefFGSWRFGSRG123412412412",
            "password2": "qweqwsadfasefFGSWRFGSRG123412412412",
            "years_of_experience": 4,
        }

        response = self.client.post(COOK_CREATE_URL, data=data)
        self.assertEqual(Cook.objects.count(), 2)
        self.assertEqual(Cook.objects.first().username, "test2")
        self.assertEqual(response.status_code, 302)

    def test_cook_list_retrieve(self):
        Cook.objects.create(
            username="user",
            password="test1",
            years_of_experience=5
        )
        Cook.objects.create(
            username="user1",
            password="test12",
            years_of_experience=5
        )
        cooks = Cook.objects.all()
        response = self.client.get(COOK_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")
