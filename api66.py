import requests

def send_request(phone_number):
    # API endpoint
    url = "https://store.focallurebd.com/api/v1/1/ecom/auth/getCode"

    # Data payload
    data = {
        "mobile": phone_number
    }

    # Headers
    headers = {
        "user-agent": "Dart/2.14 (dart:io)",
        "content-type": "application/json"
    }

    try:
        # Sending POST request with JSON payload
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()  # Return the server response in JSON format
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}