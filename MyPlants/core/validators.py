from django.core.exceptions import ValidationError


def capital_letter_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letter_validator(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")