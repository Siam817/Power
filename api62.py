import requests

def send_request(phone_number):
    # API endpoint
    url = "https://api.garibookadmin.com/api/v3/user/login"

    # Headers
    headers = {
        "User-Agent": "Dart/3.4 (dart:io)",
        "Authorization": "Bearer",
        "Content-Type": "application/json",
        "Host": "api.garibookadmin.com"
    }

    # JSON payload
    data = {
        "mobile": phone_number,
        "gb_code": "IKiyBy55yYkaF8U"
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}