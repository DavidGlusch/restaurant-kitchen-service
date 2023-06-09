from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(
        to=DishType,
        null=True,
        on_delete=models.SET_NULL,
        related_name="dishes",
    )
    cooks = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="dishes",

    )

    class Meta:
        verbose_name_plural = "dishes"
        ordering = ["name"]

    def __str__(self) -> str:
        return str(self.name)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"
