import pytest
from tests import (client, post_json, put_json)


def test_post_order(client):
    """test posting order"""
    resp = post_json(client, '/v1/orders', {
        "customer_name": "Nangai",
        "item_name": "Chicken",
        "quantity": 5, })
    assert resp.status_code == 201
    assert b'Order has been added' in resp.data


def test_get_orders(client):
    resp = client.get(
        '/v1/orders')
    assert b'customer_name' in resp.data
    assert b'Nangai' in resp.data
    assert b'Chicken' in resp.data
    assert resp.status_code == 200


def test_get_single_order(client):
    """test get single order"""
    resp = client.get('/v1/orders/1/')
    assert resp.status_code == 200
    assert b'customer_name' in resp.data


def test_get_wrong_order(client):
    resp = client.get('/v1/orders/2/')
    assert resp.status_code == 404
    assert b'Order not found' in resp.data


def test_update_order(client):
    resp = put_json(client, '/v1/orders/1/', {
        "status": "complete", })
    assert resp.status_code == 201


def test_update_non_existing_order(client):
    resp = put_json(client, '/v1/orders/2/', {
        "status": "complete", })
    assert b'Order not found' in resp.data
    assert resp.status_code == 404
