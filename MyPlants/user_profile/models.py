from django.core.validators import MinLengthValidator
from django.db import models

from MyPlants.core.validators import capital_letter_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)]
    )

    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[capital_letter_validator]
    )

    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[capital_letter_validator]
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
