from flask import Flask, request

from intelligence import calculate_waiting_time, get_queue_status

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "QueueSense backend is running"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return {
            "error": "Request body must contain JSON data"
        }, 400

    if "queue_count" not in data:
        return {
            "error": "queue_count is required"
        }, 400

    if "service_rate" not in data:
        return {
            "error": "service_rate is required"
        }, 400

    queue_count = data["queue_count"]
    service_rate = data["service_rate"]

    if not isinstance(queue_count, (int, float)):
        return {
            "error": "queue_count must be a number"
        }, 400

    if not isinstance(service_rate, (int, float)):
        return {
            "error": "service_rate must be a number"
        }, 400

    if queue_count < 0:
        return {
            "error": "queue_count cannot be negative"
        }, 400

    if service_rate <= 0:
        return {
            "error": "service_rate must be greater than 0"
        }, 400

    waiting_time = calculate_waiting_time(queue_count, service_rate)
    status = get_queue_status(queue_count)

    return {
    "queue_count": queue_count,
    "service_rate": service_rate,
    "waiting_time": waiting_time,
    "status": status
    }

if __name__ == "__main__":
    app.run(debug=True)