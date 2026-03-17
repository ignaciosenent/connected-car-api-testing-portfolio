# Connected Car API Testing Portfolio

API test automation portfolio project built with **Python**, **pytest**, and **requests** to validate key functional flows of a **vehicle connectivity platform**.

This project focuses on realistic automotive connectivity scenarios such as authentication, vehicle access, vehicle status retrieval, location checks, remote commands, and authorization validation.

## Project Goal

The goal of this project is to demonstrate API test automation skills applied to a domain close to real-world **connected vehicle / telematics systems**.

Rather than testing a generic public API, this portfolio simulates business-relevant use cases such as:

- user authentication
- access to paired vehicles
- vehicle status retrieval
- vehicle location retrieval
- remote lock/unlock commands
- authorization checks for unauthorized vehicles

## Tech Stack

- **Python**
- **pytest**
- **requests**
- **Flask** (for the mock API)
- **Git / GitHub**

## Project Structure

```text
connected-car-api-testing-portfolio/
├─ config/
│  └─ settings.py
├─ data/
│  └─ test_data.py
├─ mock_api/
│  └─ app.py
├─ tests/
│  ├─ test_auth.py
│  ├─ test_authorization.py
│  ├─ test_remote_commands.py
│  ├─ test_vehicle_status.py
│  └─ test_vehicles.py
├─ utils/
│  ├─ api_client.py
│  └─ assertions.py
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ README.md