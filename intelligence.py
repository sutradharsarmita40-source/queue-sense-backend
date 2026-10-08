def calculate_waiting_time(queue_count, service_rate):
    return queue_count / service_rate


def get_queue_status(queue_count):
    if queue_count <= 3:
        return "low"

    if queue_count <= 7:
        return "moderate"

    return "high"