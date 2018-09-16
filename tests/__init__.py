"""file contains methods used in the other tests files"""
import http.client
import pytest
from app.views import app
import json

@pytest.fixture
def client():
    client = app.test_client()
    yield client
