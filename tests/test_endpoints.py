import pytest
from tests import (client)

def test_get_endpoint(client):
    resp = client.get(
        '/')
    assert resp.status_code == 200