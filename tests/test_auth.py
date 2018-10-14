import pytest
from tests import (client, post_json, database)


def test_user_creation(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "test@test.com",
            "name": "test",
            "password": "testAs1v",
            "role": "True"
        })
    assert b'User successfully created' in resp.data
    assert resp.status_code == 201


def test_duplicate_user_creation(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "test@test.com",
            "name": "test",
            "password": "testAs1v",
            "role": "True"
        })
    assert b'Email address already exists' in resp.data
    assert resp.status_code == 400


def test_user_login(client, database):
    resp = post_json(client, '/v1/auth/login', {
        "email": "test@test.com",
        "password": "testAs1v"
    })
    assert b'Successful login' in resp.data
    assert resp.status_code == 200


def test_user_bad_login(client, database):
    resp = post_json(client, '/v1/auth/login', {
        "email": "test@test.com",
        "password": "tessfsgeat"
    })
    assert b'Bad username' in resp.data
    assert resp.status_code == 400


def test_long_name(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "test@test.com",
            "name": "testismeyoutoova",
            "password": "testsfas",
            "role": "True"
        })
    assert b'Max 15' in resp.data
    assert resp.status_code == 400


def test_invalid_name(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "test@test.com",
            "name": "testAsBA",
            "password": "testsfas",
            "role": "True"
        })
    assert b'Name can only contain lowercase a-z, 0-9' in resp.data
    assert resp.status_code == 400


def test_short_password(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "jks@test.com",
            "name": "test",
            "password": "test",
            "role": "True"
        })
    assert b'Password should be 8 chars at least' in resp.data
    assert resp.status_code == 400


def test_long_password(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "test@test.com",
            "name": "test",
            "password": "testsfsfdsfsdf",
            "role": "True"
        })
    assert b'12 at most' in resp.data
    assert resp.status_code == 400


def test_invalid_email(client, database):
    resp = post_json(
        client, '/v1/auth/signup', {
            "email": "testtest",
            "name": "test",
            "password": "testsftd",
            "role": "True"
        })
    assert b'Invalid email' in resp.data
    assert resp.status_code == 400


def test_empty_post_email(client):
    resp = post_json(client, '/v1/auth/signup', {"email": " "})
    assert resp.status_code == 400
    assert b'Email field is empty' in resp.data
    assert b'Name field is empty' in resp.data
    assert b'Password field is empty' in resp.data
    assert b'Role field is empty' in resp.data


def test_empty_post_name(client):
    resp = post_json(client, '/v1/auth/signup',
                     {"email": "arthur.nangai@gmail.com"})
    assert resp.status_code == 400
    assert b'Name field is empty' in resp.data
    assert b'Password field is empty' in resp.data
    assert b'Role field is empty' in resp.data


def test_empty_post_password(client):
    resp = post_json(client, '/v1/auth/signup',
                     {"email": "arthur.nangai@gmail.com", "name": "arty"})
    assert resp.status_code == 400
    assert b'Password field is empty' in resp.data
    assert b'Role field is empty' in resp.data

def test_empty_post_role(client):
    resp = post_json(client, '/v1/auth/signup',
                     {"email": "arthur.nangai@gmail.com", "name": "arty", "password":"ljfls"})
    assert resp.status_code == 400
    assert b'Role field is empty' in resp.data
