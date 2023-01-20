import pytest


# TODO: создание объявления — POST /ad/

@pytest.mark.django_db
def test_ads_create(client, admin_token):
    expected_response = {
        "id": 1,
        "category": None,
        "locations": [],
        "slug": "test_slug",
        "name": "text test_django",
        "price": 1,
        "is_published": False,
        "author": "test",
        "image": None,
        "description": None,
    }

    data = {
        "name": "text test_django",
        "category": "",
        "slug": "test_slug",
        "is_published": False,
        "author": "test",
        "price": "1"
    }

    response = client.post(
        "/ad/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + admin_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
