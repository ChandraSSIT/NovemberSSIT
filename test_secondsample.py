import json
import pytest
import requests
import random
from confest import *


@pytest.mark.smoke
@pytest.mark.usefixtures("get_authorization_token")
def test_create_user_with_token(get_authorization_token):
    token = get_authorization_token
    url = "https://gorest.co.in/public/v2/users"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    temp = random.randint(0,100)
    mail = "test"+str(temp)+"@gmail.org.com"

    payload = payload = json.dumps({
        "name": "Gajbaahu Mukhopadhyay",
        "email":mail,
        "gender": "male",
        "status": "active"
    })
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None


@pytest.mark.usefixtures("get_authorization_token")
def test_update_user(get_authorization_token):
    token = get_authorization_token
    url = "https://gorest.co.in/public/v2/users/1"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "name": "Chandan",
        "email": "chandan_rana@little.info",
        "gender": "male",
        "status": "active"
    })
    response = requests.put(url, headers=headers, data=payload)
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "Chandan"
