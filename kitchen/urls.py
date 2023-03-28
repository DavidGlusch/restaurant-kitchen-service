from django.urls import path

from kitchen.views import (
    index,
    # DishTypeDetailView,
    DishTypeListView,
    DishDetailView,
    DishListView,
    CookDetailView,
    CookListView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    # path("dish-type/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-detail"),

    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>", DishDetailView.as_view(), name="dish-detail"),

    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>", CookDetailView.as_view(), name="cook-detail"),

]

app_name = "kitchen"
