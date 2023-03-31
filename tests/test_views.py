from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType, Cook

DISH_TYPE_URL = reverse("kitchen:dish-type-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")


class PublicDishTypeTest(TestCase):
    def test_cook_login_required(self):
        response = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(response, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test1234567",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="test1")
        DishType.objects.create(name="test2")

        response = self.client.get(DISH_TYPE_URL)
        dish_type = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_type_list"]),
                         list(dish_type))
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_dish_type_search(self):
        DishType.objects.create(name="test1").filter(name__icontains="t")
        response = self.client.get(DISH_TYPE_URL + "?name=t")
        self.assertEqual(response.status_code, 200)
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

    def test_retrieve_dish(self):
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

    def test_dish_search(self):
        Dish.objects.create(
            name="test1",
            price=5.1
        ).filter(name__icontains="t")
        response = self.client.get(DISH_URL + "?name=t")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test2",
        )
        self.client.force_login(self.user)

    def test_retrieve_cook_list(self):
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

    def test_cook_search(self):
        Cook.objects.create(
            username="user",
            password="test1",
            years_of_experience=5
        ).filter(username__icontains="u")
        response = self.client.get(COOK_URL + "?username=u")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_list.html")
