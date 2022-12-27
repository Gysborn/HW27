from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

class User(models.Model):
    ROLE = [
        ("member", "Член"),
        ("moderator", "Модератор"),
        ("admin", "Администратор")
    ]

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=9, choices=ROLE, default="member")
    age = models.PositiveSmallIntegerField()
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


