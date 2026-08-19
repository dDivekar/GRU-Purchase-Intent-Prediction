import unittest
from fastapi.testclient import TestClient
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app import app

class TestPurchaseIntentAPI(unittest.TestCase):
    def setUp(self):
        from backend.database import init_db
        try:
            init_db()
        except Exception as e:
            print(f"Test Setup DB init warning: {e}")
        self.client = TestClient(app)

    def test_health_check(self):
        """Test the /health endpoint."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "service": "GRU Predictor"})

    def test_predict_endpoint_valid(self):
        """Test the /predict/ endpoint with valid session inputs."""
        payload = {"session_ids": [101, 102, 103, 104]}
        response = self.client.post("/predict/", json=payload)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("purchase_probability", data)
        self.assertIn("prediction", data)
        self.assertIsInstance(data["purchase_probability"], float)
        self.assertIn(data["prediction"], ["Purchase", "No Purchase"])

    def test_predict_endpoint_invalid_format(self):
        """Test /predict/ endpoint with invalid session input format."""
        payload = {"session_ids": ["abc", "def"]}
        response = self.client.post("/predict/", json=payload)
        self.assertIn(response.status_code, [400, 422])

if __name__ == "__main__":
    unittest.main()
