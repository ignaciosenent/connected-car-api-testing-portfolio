from config.settings import AUTHORIZED_VEHICLE_ID

def test_get_vehicle_status(authenticated_client):
    response = authenticated_client.get_vehicle_status(AUTHORIZED_VEHICLE_ID)

    assert response.status_code == 200
    data = response.json()
    assert "doorsLocked" in data
    assert "engineOn" in data
    assert isinstance(data["doorsLocked"], bool)
    assert isinstance(data["engineOn"], bool)


def test_get_vehicle_location(authenticated_client):
    response = authenticated_client.get_vehicle_location(AUTHORIZED_VEHICLE_ID)

    assert response.status_code == 200
    data = response.json()
    assert "latitude" in data
    assert "longitude" in data