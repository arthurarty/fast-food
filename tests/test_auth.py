import pytest
from tests import (client, post_json, database)
from app.models.user import User


def test_is_instance_of_user():
    new_user = User("arthur.nangai@gmail.com", "Arthur Nangai", "Nangai", 0)
    assert isinstance(new_user, User)


def test_user_creation(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "test",
        "password": "testAs1v",
        "role": "True"})
    assert b'User successfully created' in resp.data
    assert resp.status_code == 201


def test_duplicate_user_creation(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "test",
        "password": "testAs1v",
        "role": "True"})
    assert b'Email address already exists' in resp.data
    assert resp.status_code == 400


def test_user_login(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "test",
        "password": "testAs1v",
        "role": "True"})
    resp = post_json(client, '/v1/auth/login', {
        "email": "test@test.com",
        "password": "testAs1v"})
    assert b'Successful login' in resp.data
    assert resp.status_code == 200


def test_long_name(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "testismeyoutoova",
        "password": "testsfas",
        "role": "True"})
    assert b'Name is too long' in resp.data
    assert resp.status_code == 400


def test_invalid_name(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "testAsBA",
        "password": "testsfas",
        "role": "True"})
    assert b'Name can only contain lowercase a-z, 0-9 and _' in resp.data
    assert resp.status_code == 400


def test_short_password(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "test",
        "password": "test",
        "role": "True"})
    assert b'Password too short' in resp.data
    assert resp.status_code == 400


def test_long_password(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "test@test.com",
        "name": "test",
        "password": "testsfsfdsfsdf",
        "role": "True"})
    assert b'Password too long' in resp.data
    assert resp.status_code == 400


def test_invalid_email(client, database):
    resp = post_json(client, '/v1/auth/signup', {
        "email": "testtest",
        "name": "test",
        "password": "testsfsfdsfsdf",
        "role": "True"})
    assert b'Invalid email' in resp.data
    assert resp.status_code == 400


def test_empty_post_email(client):
    resp = post_json(client, '/v1/auth/signup', {
        "email": " "})
    assert resp.status_code == 400
