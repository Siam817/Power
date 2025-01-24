import requests
import json

def send_request(phone_number):
    url = "https://api.apex4u.com/api/auth/login"

    headers = {
        "Content-Type": "application/json"
    }

    # Prepare the JSON payload
    data = {
        "phoneNumber": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}