from flask import Flask, jsonify, request

app = Flask(__name__)

VALID_EMAIL = "qa@test.com"
VALID_PASSWORD = "123456"
VALID_TOKEN = "fake-jwt-token"

USER_VEHICLES = [
    {"vehicleId": "VF3WC8HZC34413350", "model": "Peugeot 207", "nickname": "My Car"}
]

VEHICLE_STATUS = {
    "VF3WC8HZC34413350": {
        "doorsLocked": True,
        "engineOn": False
    }
}

VEHICLE_LOCATION = {
    "VF3WC8HZC34413350": {
        "latitude": 37.3891,
        "longitude": -5.9845
    }
}


def is_authorized(req):
    auth_header = req.headers.get("Authorization")
    return auth_header == f"Bearer {VALID_TOKEN}"


@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    if data["email"] == VALID_EMAIL and data["password"] == VALID_PASSWORD:
        return jsonify({"token": VALID_TOKEN}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(USER_VEHICLES), 200


@app.route("/vehicles/<vehicle_id>/status", methods=["GET"])
def get_vehicle_status(vehicle_id):
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if vehicle_id != "VF3WC8HZC34413350":
        return jsonify({"error": "Forbidden"}), 403

    return jsonify(VEHICLE_STATUS[vehicle_id]), 200


@app.route("/vehicles/<vehicle_id>/location", methods=["GET"])
def get_vehicle_location(vehicle_id):
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if vehicle_id != "VF3WC8HZC34413350":
        return jsonify({"error": "Forbidden"}), 403

    return jsonify(VEHICLE_LOCATION[vehicle_id]), 200


@app.route("/vehicles/<vehicle_id>/commands/lock", methods=["POST"])
def lock_vehicle(vehicle_id):
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if vehicle_id != "VF3WC8HZC34413350":
        return jsonify({"error": "Forbidden"}), 403

    return jsonify({
        "commandId": "CMD_LOCK_001",
        "status": "ACCEPTED"
    }), 202


@app.route("/vehicles/<vehicle_id>/commands/unlock", methods=["POST"])
def unlock_vehicle(vehicle_id):
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if vehicle_id != "VF3WC8HZC34413350":
        return jsonify({"error": "Forbidden"}), 403

    return jsonify({
        "commandId": "CMD_UNLOCK_001",
        "status": "ACCEPTED"
    }), 202


if __name__ == "__main__":
    app.run(debug=True, port=5000)