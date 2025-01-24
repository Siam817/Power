import requests

def send_request(phone_number):
    url = "https://hungry.express/api/v1/auth/login"
    headers = {
        "User-Agent": "Dart/3.5 (dart:io)",
        "Content-Type": "application/json",
        "Host": "hungry.express",
    }
    payload = {
        "phone": f"+88{phone_number}",
        "login_type": "otp",
        "guest_id": "22860"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"