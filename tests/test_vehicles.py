def test_get_user_vehicles(authenticated_client):
    response = authenticated_client.get_vehicles()

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "vehicleId" in data[0]