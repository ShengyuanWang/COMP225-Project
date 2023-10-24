import pytest
import sys
sys.path.append(".")
from app import app as flask_app

"""Configuration file for pytests."""

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()