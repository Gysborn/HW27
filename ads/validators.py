from django.core.exceptions import ValidationError


def not_in_status_validator(value: bool):

    if value:
        raise ValidationError("Incorrect status.")



