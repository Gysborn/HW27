import pytest

from tests.factories import AdFactory


# TODO: создание подборки — POST /selection/

@pytest.mark.django_db
def test_create_selection(client, admin_token):
    ads = AdFactory.create_batch(10)
    expected_response = {
        "id": 1,
        "owner": "admin",
        "name": "new test selection items",
        "items":  [2, 3, 5],
    }

    data = {
        "id": 1,
        "owner": "admin",
        "name": "new test selection items",
        "items": [2, 3, 5],
    }

    response = client.post(
        "/selection/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + admin_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
