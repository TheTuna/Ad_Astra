# packages import section
import pytest
from playwright.sync_api import Page
from app import app as ci_app

# setting development server for tests
@pytest.fixture(scope="session")
def app():
    
    app = ci_app
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app):
    
    return app.test_client()

# test webapp is running 
def test_app_running(client):
   
    response = client.get("/")
    assert response.status_code == 200

# test webapp returns json data from /quote endpoint
def test_data_endpoint(client):

    response = client.get("/quote")
    assert len(response.json) != None