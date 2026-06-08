import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app

def test_health():
      client = app.test_client()
      response = client.get('/health')
      assert response.status_code == 200
      data = response.get_json()
      assert data['status'] == 'healthy'

def test_users():
      client = app.test_client()
      response = client.get('/api/users')
      assert response.status_code == 200
      data = response.get_json()
      assert len(data['users']) == 2
