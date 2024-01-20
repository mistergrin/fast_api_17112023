from fastapi import status


def test_root_status(client):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK


def test_root_content(client):
    response = client.get('/')
    assert response.json() == {'try': "ok", "count": 10, "bool": True}
