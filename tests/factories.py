import factory.django

from ads.models import Ad
from authentications.models import User


class SelectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_select_factory"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test"
    password = "1234"
    role = "admin"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_factory"
    slug = "test_slug"
    price = 1
    author_id = 1
    description = "test factory detail"
    image = None
    is_published = False
