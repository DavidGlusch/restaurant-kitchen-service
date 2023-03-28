from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    dish_type = models.ForeignKey(
        to=DishType,
        on_delete=models.SET_NULL,
        related_name="dishes",
    )

    class Meta:
        verbose_name_plural = "dishes"
        ordering = ["name"]
