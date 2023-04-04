from unittest import TestCase

from kitchen.forms import CookSearchForm, DishTypeSearchForm, DishSearchForm


class DishTypeSearchFormTest(TestCase):
    def test_dish_type_search_by_name(self):
        form_data = {"name": "test"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test")


class DishSearchFormTest(TestCase):
    def test_dish_search_by_name(self):
        form_data = {"name": "test"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test")


class CookSearchFormTest(TestCase):
    def test_cook_search_by_username(self):
        form_data = {"username": "test"}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "test")
