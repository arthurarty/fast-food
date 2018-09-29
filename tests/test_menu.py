import pytest
from tests import (client, post_json, put_json,
                   post_json_header, signin, user_two)


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


def test_post_menu_empty_name(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": " ",
        "desc": "fried chapati",
        "price": 2000},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 400
    assert b'Name must be a string' in resp.data


def test_post_menu_no_name(client):
    resp = post_json_header(client, '/v1/menu', {
        "desc": "fried chapati",
        "price": 2000},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 400
    assert b'Food_name is missing' in resp.data


def test_post_menu_no_desc(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": "chicken",
        "price": 2000},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 400
    assert b'Desc is missing' in resp.data


def test_post_menu_empty_desc(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": "chicken",
        "desc": " ",
        "price": 2000},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 400
    assert b'Desc name must be a string' in resp.data


def test_post_menu_no_price(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": "chicken",
        "desc": "deep fried"},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 400
    assert b'Price is missing' in resp.data


def test_post_menu_empty_price(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": "chicken",
        "desc": "deep fried",
        "price": 0.5},
        headers={'Authorization': 'Bearer ' + signin(client)})
    assert resp.status_code == 400
    assert b'Price must be an integer' in resp.data


def test_add_item_by_user(client):
    resp = post_json_header(client, '/v1/menu', {
        "food_name": "chap",
        "desc": "fried chap",
        "price": 3500},
        headers={'Authorization': 'Bearer ' + user_two(client)})
    assert resp.status_code == 401
    assert b'Not authorized' in resp.data
