from django.db import models
from django.core.validators import MinLengthValidator

from MyPlants.core.validators import only_letter_validator


class Plant(models.Model):
    PLANT_TYPE = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    plant_type = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        choices=PLANT_TYPE,
    )

    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), only_letter_validator]
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
