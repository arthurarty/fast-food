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

@pytest.fixture(scope='module')
def database():
    db_conn = Database()
    yield db_conn
    db_conn.drop_table('users')

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def put_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.put(url, data=json.dumps(json_dict), content_type='application/json')
