"""file contains methods used in the other tests files"""
import http.client
import pytest
from app.views import app
from app.models import Database
import json
import os


@pytest.fixture
def client():
    client = app.test_client()
    yield client


@pytest.fixture(scope='session')
def database():
    db_conn = Database()
    yield db_conn
    db_conn.drop_all_tables()


def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def post_json_header(client, url, json_dict, headers):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)

def put_json(client, url, json_dict, headers):
    """Send dictionary json_dict as a json to the specified url """
    return client.put(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

def signin(client):
    resp = post_json(client, '/v1/auth/login', {
        "email": "test@test.com",
        "password": "testAs1v"})
    access = json_of_response(resp)
    access_token = access[1]['access_token']
    return access_token
