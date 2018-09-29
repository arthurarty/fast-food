import pytest
from tests import (client, post_json, put_json, post_json_header, signin)


def test_get_menu(client):
    resp = client.get(
        '/v1/menu', headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 200


def test_post_menu(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": "chapati",
        "desc": "fried chapati",
        "price": 2000},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 201
    assert b'Food has been added' in resp.data
