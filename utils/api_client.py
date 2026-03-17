import requests
from config.settings import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.token = None

    def login(self, payload):
        return requests.post(f"{self.base_url}/auth/login", json=payload)

    def set_token(self, token):
        self.token = token

    def _headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get_vehicles(self):
        return requests.get(f"{self.base_url}/vehicles", headers=self._headers())

    def get_vehicle_status(self, vehicle_id):
        return requests.get(
            f"{self.base_url}/vehicles/{vehicle_id}/status",
            headers=self._headers()
        )

    def get_vehicle_location(self, vehicle_id):
        return requests.get(
            f"{self.base_url}/vehicles/{vehicle_id}/location",
            headers=self._headers()
        )

    def lock_vehicle(self, vehicle_id):
        return requests.post(
            f"{self.base_url}/vehicles/{vehicle_id}/commands/lock",
            headers=self._headers()
        )

    def unlock_vehicle(self, vehicle_id):
        return requests.post(
            f"{self.base_url}/vehicles/{vehicle_id}/commands/unlock",
            headers=self._headers()
        )