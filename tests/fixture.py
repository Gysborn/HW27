import pytest


@pytest.fixture
@pytest.mark.django_db
def admin_token(client, django_user_model):
    username = "admin"
    password = "1234"

    django_user_model.objects.create_user(
        username=username, password=password, role="admin"
    )

    response = client.post(
        "/user/login/",
        {"username": username, "password": password},
        format="json",
    )

    return response.data["token"]
