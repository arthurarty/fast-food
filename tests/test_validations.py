# import pytest
# from tests import (client, post_json, put_json, post_json_header, signin)

# def test_empty_customer_name(client):
#     """post data without value customer name"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": " ",
#         "item_name": "Chapati",
#         "quantity": "5", }, 
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Name must be a string' in resp.data
#     assert resp.status_code == 400


# def test_no_customer_name(client):
#     """post data without customer_name"""
#     resp = post_json_header(client, '/v1/orders', {
#         "item_name": "Chapati",
#         "quantity": "5", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Customer_name missing' in resp.data
#     assert resp.status_code == 400


# def test_empty_item_name(client):
#     """post data without with value for item name"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "Nangai",
#         "item_name": " ",
#         "quantity": "5", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Item name must be a string' in resp.data
#     assert resp.status_code == 400


# def test_no_item_name(client):
#     """post data without item_name field"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "Nangai",
#         "quantity": "5", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Item_name missing' in resp.data
#     assert resp.status_code == 400


# def test_empty_quantity(client):
#     """post data without value for item name"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "Nangai",
#         "item_name": "Matooke",
#         "quantity": "", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Quantity is missing' in resp.data
#     assert resp.status_code == 400

# def test_zero_quantity(client):
#     """post data without value for item name"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "Nangai",
#         "item_name": "Matooke",
#         "quantity": 0, },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Quantity is missing' in resp.data
#     assert resp.status_code == 400

# def test_empty_status(client):
#     """post data without value for item name"""
#     resp = put_json(client, '/v1/orders/1/', {
#         "status": " ", }, 
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Status input has to be complete' in resp.data
#     assert resp.status_code == 400


# def test_no_quantity(client):
#     """post data without quantity field"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "Nangai",
#         "item_name": "Matooke", },
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Quantity is missing' in resp.data
#     assert resp.status_code == 400


# def test_int_customer_name(client):
#     """test validation for customer_name is int"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": 1543,
#         "item_name": "Matooke",
#         "quantity": 10, }, 
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Name must be a string. Example: johndoe' in resp.data
#     assert resp.status_code == 400


# def test_int_item_name(client):
#     """test validation for item_name is int"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "John",
#         "item_name": 12,
#         "quantity": 10, }, 
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Item name must be a string. Example: Rice' in resp.data
#     assert resp.status_code == 400


# def test_str_quantity(client):
#     """test validation for quantity as str"""
#     resp = post_json_header(client, '/v1/orders', {
#         "customer_name": "John",
#         "item_name": "Matooke",
#         "quantity": "10", }, 
#         headers={'Authorization': 'Bearer ' + signin(client)})
#     assert b'Quantity must be an integer > 0. Example: 2' in resp.data
#     assert resp.status_code == 400
