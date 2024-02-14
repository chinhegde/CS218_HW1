import pytest
from flask import Flask
from app import app

class MockResponse:
    @staticmethod
    def json():
        return {'products': [{'id': 1, 'name': 'Product1'}, {'id': 2, 'name': 'Product2'}]}

class MockCatResponse:
    @staticmethod
    def json():
        return {'categories': ['cat1', 'cat2']}


class MockSearchResponse:
    @staticmethod
    def json():
        return {'results': [{'id': 1, 'name': 'Product1'}]}     

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_welcome_page(client):
    response = client.get('/')
    print("RESPONSE", response.data)
    assert response.status_code == 200
    assert b'CS 218 - HW1' in response.data

def test_get_all_products(client, monkeypatch):
    print("RUNNING 23")
    def mock_get_all_products(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get_all_products)

    response = client.get('/api/products')
    print("RESPONSE", response.data)

    assert response.status_code == 200
    assert 'products' in response.json

def test_get_all_product_categories(client, monkeypatch):
    print("RUNNING 34")
    def mock_get_all_categories(*args, **kwargs):
        return MockCatResponse()

    monkeypatch.setattr('requests.get', mock_get_all_categories)

    response = client.get('/api/products/categories')
    print("RESPONSE", response.data)
    assert response.status_code == 200
    assert 'categories' in response.json

def test_search_products(client, monkeypatch):
    def mock_search_products(*args, **kwargs):
        return MockSearchResponse()

    monkeypatch.setattr('requests.get', mock_search_products)

    response = client.get('/api/products/search?q=test')
    assert response.status_code == 200
    assert 'results' in response.json

def test_get_single_product(client, monkeypatch):
    response = client.get('/api/products/1')
    assert response.status_code == 200
    assert 'id' in response.json
    assert 'title' in response.json
