from django.db import models

from ads.validators import *
from authentications.models import User


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()  # TODO: Значение поля price не может быть меньше 0. Да!
    description = models.TextField(null=True, blank=True)  # TODO: Поле description может быть пустым. Да!
    image = models.ImageField(null=True, blank=True, upload_to='pictures')
    is_published = models.BooleanField(validators=[not_in_status_validator])
    # TODO: Значение поля is_published при создании объявления не может быть True.
    category = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Selections(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"
