"""
Unit tests for the Flask application.
These tests verify the API functionality.
"""
import pytest
from src.app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'


def test_get_all_orders(client):
    """Test getting all orders without filters."""
    response = client.get('/api/orders')
    assert response.status_code == 200
    data = response.get_json()
    assert 'orders' in data
    assert 'count' in data
    assert data['count'] == 5  # We have 5 sample orders
    assert len(data['orders']) == 5


def test_filter_by_start_date(client):
    """Test filtering orders by start date."""
    response = client.get('/api/orders?start_date=2025-12-08')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 3  # Orders from Dec 8 onwards
    for order in data['orders']:
        assert order['date'] >= '2025-12-08'


def test_filter_by_end_date(client):
    """Test filtering orders by end date."""
    response = client.get('/api/orders?end_date=2025-12-05')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 2  # Orders up to Dec 5
    for order in data['orders']:
        assert order['date'] <= '2025-12-05'


def test_filter_by_date_range(client):
    """Test filtering orders by date range."""
    response = client.get('/api/orders?start_date=2025-12-05&end_date=2025-12-10')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 3  # Orders between Dec 5 and Dec 10
    for order in data['orders']:
        assert '2025-12-05' <= order['date'] <= '2025-12-10'


def test_invalid_date_format(client):
    """Test that invalid date formats return an error."""
    response = client.get('/api/orders?start_date=invalid-date')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert 'Invalid' in data['error']


def test_no_orders_in_range(client):
    """Test filtering with a date range that has no orders."""
    response = client.get('/api/orders?start_date=2025-12-20&end_date=2025-12-25')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 0
    assert len(data['orders']) == 0
