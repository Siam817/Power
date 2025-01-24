import requests

def send_request(phone_number):
    # API endpoint
    url = "https://api.pathao.com/v2/auth/register"

    # Headers
    headers = {
        "app-agent": "ride/android/478",
        "android-os": "10",
        "content-type": "application/json",
        "user-agent": "okhttp/4.12.0"
    }

    # Payload: Remove leading '0' from phone number if present
    payload = {
        "country_prefix": "880",
        "national_number": phone_number[1:],  # Remove leading '0' for the number
        "country_id": 1  # Assuming country_id 1 corresponds to Bangladesh
    }

    try:
        # Sending POST request with JSON payload
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()  # Return the server response in JSON format
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}