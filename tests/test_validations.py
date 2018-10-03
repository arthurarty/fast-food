import pytest
from tests import (client, post_json, put_json, post_json_header, signin)


def test_zero_menu_id(client):
    """post data without value customer name"""
    resp = post_json_header(client, '/v1/users/orders', {
        "menu_id": 0,
        "quantity": 15},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert b'Menu_id is missing' in resp.data
    assert resp.status_code == 400


def test_str_menu_id(client):
    """post data without value customer name"""
    resp = post_json_header(client, '/v1/users/orders', {
        "menu_id": "1",
        "quantity": 15},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert b'Menu_id and Quantity must be integers > 0. Example: 2' in resp.data
    assert resp.status_code == 400


def test_zero_quantity(client):
    """post data without value customer name"""
    resp = post_json_header(client, '/v1/users/orders', {
        "menu_id": 1,
        "quantity": 0},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert b'Quantity is missing' in resp.data
    assert resp.status_code == 400


def test_str_quantity(client):
    """post data without value customer name"""
    resp = post_json_header(client, '/v1/users/orders', {
        "menu_id": 1,
        "quantity": "12"},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert b'Menu_id and Quantity must be integers > 0. Example: 2' in resp.data
    assert resp.status_code == 400


def test_update_empty_status(client):
    resp = put_json(client, '/v1/orders/1/', {
        "status": " ", },
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert b'Status input has to be Processing, Cancelled or Complete' in resp.data
    assert resp.status_code == 400


def test_redirect(client):
    resp = client.get('/', follow_redirects=True)
    assert resp.status_code == 200


def test_route_not_found(client):
    resp = client.get('/fods')
    assert resp.status_code == 404
    assert b'Route does not exist' in resp.data
