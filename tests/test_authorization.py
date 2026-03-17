from config.settings import UNAUTHORIZED_VEHICLE_ID, AUTHORIZED_VEHICLE_ID

def test_access_vehicle_without_token(api_client):
    response = api_client.get_vehicle_status(AUTHORIZED_VEHICLE_ID)

    assert response.status_code == 401

def test_access_unpaired_vehicle(authenticated_client):
    response = authenticated_client.get_vehicle_status(UNAUTHORIZED_VEHICLE_ID)

    assert response.status_code in [403, 404]