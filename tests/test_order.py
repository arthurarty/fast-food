import pytest
from tests import (client, post_json)

def test_post_order(client):
    resp = post_json(client, '/v1/orders', {
        "customer_name": "Nangai",
        "item_name" : "Chapati", 
        "quantity" : "5", })
    assert resp.status_code == 201
