from datetime import date

from django.core.exceptions import ValidationError
from rest_framework import serializers


# def check_day_not_past(value: date):
#     age = value - date.today()
#     if age:
#         raise ValidationError(
#             "Registration is available from the age of 9"
#         )


class CheckBirthdayValidator:

    def __init__(self, age: int):
        self.age = age

    def __call__(self, value: date):
        old = date.today() - value
        if old.days < self.age:
            raise serializers.ValidationError("Registration is available from the age of 9.")
