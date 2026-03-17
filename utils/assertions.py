def assert_status_code(response, expected_code):
    assert response.status_code == expected_code

def assert_has_keys(data, expected_keys):
    for key in expected_keys:
        assert key in data