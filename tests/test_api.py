#!/usr/bin/env python3
import unittest
import requests

class TestAPIEndpoints(unittest.TestCase):
    def test_health_endpoint(self):
        response = requests.get("http://localhost:8000/health")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
