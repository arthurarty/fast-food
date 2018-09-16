"""file contains methods used in the other tests files"""
import http.client
import pytest
from app.views import app
import json


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')
