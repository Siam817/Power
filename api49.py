import requests

def send_request(phone_number):
    # API URL and headers
    url = "https://api.goldkinen.com/api/v2/auth/request-otp/"
    headers = {
        "version-code": "2.12.5",
        "user-agent": "gk-app",
        "content-type": "application/json"
    }

    # JSON payload
    payload = {
        "phone_number": phone_number,
        "scope": "registration",
        "is_resend": False
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}