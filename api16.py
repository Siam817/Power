import requests

def send_request(phone_number):
    url = "https://api.englishmojabd.com/api/v1/auth/login"
    headers = {
        "User-Agent": "Dart/3.2 (dart:io)",
        "Content-Type": "application/json"
    }
    payload = {
        "phone": f"+88{phone_number}"  # Format the phone number with country code
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"