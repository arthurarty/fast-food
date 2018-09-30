import pytest
from tests import (client, post_json, put_json, post_json_header, signin)


def test_post_order(client):
    """test posting order"""
    resp = post_json_header(client, '/v1/orders', {
        "menu_id": 1,
        "quantity": 15},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 201
    assert b'Order successfully added' in resp.data


# def test_get_orders(client):
#     resp = client.get(
#         '/v1/orders', headers={'Authorization': 'Bearer ' + signin(client)})
#     assert resp.status_code == 200


# def test_get_single_order(client):
#     """test get single order"""
#     resp = client.get(
#         '/v1/orders/1/', headers={'Authorization': 'Bearer ' + signin(client)})
#     assert resp.status_code == 200
#     assert b'customer_name' in resp.data


# def test_get_wrong_order(client):
#     resp = client.get(
#         '/v1/orders/2/', headers={'Authorization': 'Bearer ' + signin(client)})
#     assert resp.status_code == 404
#     assert b'Order not found' in resp.data


# def test_update_order(client):
#     resp = put_json(client, '/v1/orders/1/', {
#         "status": "complete", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert resp.status_code == 201


# def test_update_non_existing_order(client):
#     resp = put_json(client, '/v1/orders/2/', {
#         "status": "complete", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Order not found' in resp.data
#     assert resp.status_code == 404
