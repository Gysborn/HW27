import pytest

# TODO: выдачу одного объявления — GET /ad/<ad_id>/

@pytest.mark.django_db
def test_detail_ad(client, ad, admin_token):
    expected_response = {
        "id": 1,
        "category": None,
        "slug": "test_slug",
        "name": "test_factory",
        "price": 1,
        "is_published": False,
        "author": 1,
        "image": None,
        "description": "test factory detail",
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Token " + admin_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
