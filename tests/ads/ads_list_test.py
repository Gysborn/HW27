import pytest

from ads.models import Ad, Categories
from authentications.models import User

# TODO: выдачу списка объявлений (без фильтров) — GET /ad

@pytest.mark.django_db
def test_list_ads(client):
    cat = Categories.objects.create(
        name="Котики"
    )
    user = User.objects.create(
        username="test",
        password="1234"
    )
    ad = Ad.objects.create(
        name="test ad",
        slug="test_ad",
        is_published=False,
        price=1,
        author_id=user.pk,
        category_id=cat.pk,
    )

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": ad.pk,
            "name": "test ad",
            "slug": "test_ad",
            "author": ad.author.username,
            "is_published": False,
            "category": ad.category.name,
            "price": 1,
            "locations": [],
            'description': None,
            'image': None
        }]
    }

    response = client.get("/ad/")
    assert response.status_code == 200
    assert response.data == expected_response
