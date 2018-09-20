import pytest
from tests import (client, post_json)


def test_empty_customer_name(client):
    """post data without customer name"""
    resp = post_json(client, '/v1/orders', {
        "customer_name": " ",
        "item_name": "Chapati",
        "quantity": "5", })
    assert resp.status_code == 400


def test_empty_item_name(client):
    """post data without item name"""
    resp = post_json(client, '/v1/orders', {
        "customer_name": "Nangai",
        "item_name": " ",
        "quantity": "5", })
    assert resp.status_code == 400

def test_empty_quantity(client):
    """post data without item name"""
    resp = post_json(client, '/v1/orders', {
        "customer_name": "Nangai",
        "item_name": "Matooke",
        "quantity": "", })
    assert resp.status_code == 400

def test_int_customer_name(client):
    """test status code returned when customer_name is int"""
    resp = post_json(client, '/v1/orders', {
        "customer_name": 1543,
        "item_name": "Matooke",
        "quantity": 10, })
    assert b'Name must be a string. Example: johndoe' in resp.data
    assert resp.status_code == 400