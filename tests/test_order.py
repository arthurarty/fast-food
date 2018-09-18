import pytest
from tests import (client, post_json)


def test_post_order(client):
    """test posting order"""
    resp = post_json(client, '/v1/orders', {
        "customer_name": "Nangai",
        "item_name": "Chapati",
        "quantity": "5", })
    assert resp.status_code == 201
    assert b'Order has been added' in resp.data


def test_get_orders(client):
    resp = client.get(
        '/v1/orders')
    assert b'customer_name' in resp.data
    assert resp.status_code == 200


def test_get_single_order(client):
    resp = client.get('/v1/orders/1/')
    assert resp.status_code == 200
    assert b'customer_name' in resp.data


def test_update_order(client):
    resp = client.put('/v1/orders/1/')
    assert resp.status_code == 201
