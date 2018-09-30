import pytest
from tests import (client, post_json, put_json, post_json_header, signin, user_two)


def test_post_order(client):
    """test posting order"""
    resp = post_json_header(client, '/v1/users/orders', {
        "menu_id": 1,
        "quantity": 15},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 201
    assert b'Order successfully added' in resp.data

def test_post_order_wrong_menu_id(client):
    """test posting order"""
    resp = post_json_header(client, '/v1/users/orders', {
        "menu_id": 2,
        "quantity": 15},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 404
    assert b'Menu Item does not exist' in resp.data

def test_get_orders_by_admin(client):
    resp = client.get(
        '/v1/orders', headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 200

def test_get_users_history(client):
    resp = client.get(
        '/v1/users/orders', headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 200
    assert b'order_id' in resp.data

def test_get_orders_by_user(client):
    resp = client.get(
        '/v1/orders', headers={'Authorization': 'Bearer ' + user_two(client)})
    assert resp.status_code == 401
    assert b'Not authorized' in resp.data
    
def test_get_single_order(client):
    """test get single order"""
    resp = client.get(
        '/v1/orders/1/', headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 200
    assert b'order_id' in resp.data

def test_get_single_order_by_user(client):
    """test to ensure users cant view specific order"""
    resp = client.get(
        '/v1/orders/1/', headers={'Authorization': 'Bearer ' + user_two(client)})
    assert resp.status_code == 401
    assert b'Not authorized' in resp.data

def test_get_wrong_order(client):
    resp = client.get(
        '/v1/orders/2/', headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 404
    assert b'Order not found' in resp.data


def test_update_order(client):
    resp = put_json(client, '/v1/orders/1/', {
        "status": "Complete", },
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 201

def test_update_order_by_user(client):
    """test to ensure users cant view specific order"""
    resp = put_json(client, '/v1/orders/1/', {
        "status": "Complete", },
        headers={'Authorization': 'Bearer ' + user_two(client)})
    assert resp.status_code == 401
    assert b'Not authorized' in resp.data

def test_update_non_existing_order(client):
    resp = put_json(client, '/v1/orders/2/', {
        "status": "Complete", },
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert b'Order not found' in resp.data
    assert resp.status_code == 404
