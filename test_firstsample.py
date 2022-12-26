import pytest
import requests
import json


@pytest.mark.smoke
def test_get_users():
    url = 'https://gorest.co.in/public/v2/users'
    headers = {}
    payload = {}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    assert result[0]["name"] is not None


def test_get_users_invalid():
    url = 'https://gorest.co.in/pjsjkdhfksdublic/v2/users'
    headers = {}
    payload = {}
    response = requests.get(url, headers=headers)
    assert response.status_code == 404


def test_create_user():
    url = "https://reqres.in/api/users"
    payload = json.dumps({
        "name": "Chandra",
        "job": "leader"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Chandra"
    assert result["id"] is not None
    assert result["job"] == "leader"


def test_update_user():
    first_name = "Janet warner"
    last_name = "Weave asdsadr"
    payload = json.dumps(
        {
            "first_name": first_name,
            "last_name": last_name
        }
    )
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put("https://reqres.in/api/users/2", headers=headers, data=payload)
    assert response.status_code == 200
    result = response.json()
    assert result["first_name"] == first_name
    assert result["last_name"] == last_name
    assert result["updatedAt"] is not None


def test_delete_user(id):
    url = f"https://reqres.in/api/users/{id}"
    response = requests.delete(url)
    assert response.status_code == 204
