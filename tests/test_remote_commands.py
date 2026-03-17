from config.settings import AUTHORIZED_VEHICLE_ID

def test_lock_vehicle(authenticated_client):
    response = authenticated_client.lock_vehicle(AUTHORIZED_VEHICLE_ID)

    assert response.status_code == 202
    data = response.json()
    assert "commandId" in data
    assert data["status"] in ["PENDING", "ACCEPTED", "COMPLETED"]

def test_unlock_vehicle(authenticated_client):
    response = authenticated_client.unlock_vehicle(AUTHORIZED_VEHICLE_ID)

    assert response.status_code == 202
    data = response.json()
    assert "commandId" in data