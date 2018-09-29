import pytest
from tests import (client, post_json, put_json, post_json_header, signin)

def test_get_menu(client):
    resp = client.get(
        '/v1/menu', headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 200
