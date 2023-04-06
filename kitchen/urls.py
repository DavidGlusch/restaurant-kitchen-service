from django.urls import path

from kitchen.views import (
    index,

    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishDetailView,
    DishListView,
    DishCreateView,
    DishDeleteView,
    DishUpdateView,
    CookDetailView,
    CookListView,
    CookCreateView,
    CookDeleteView,
    CookYearsOfExperienceUpdateView,
    DishTypeDetailView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish-type/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dish-type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path(
        "dish-type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),


    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),

    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cook/<int:pk>/update/",
        CookYearsOfExperienceUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),

]

app_name = "kitchen"
