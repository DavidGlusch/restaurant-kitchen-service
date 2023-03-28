from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Dish, DishType, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
