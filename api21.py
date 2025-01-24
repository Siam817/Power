import requests

def send_request(phone_number):
    url = "https://api.ostad.app/api/v2/user/with-otp"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://ostad.app",
    }
    payload = {"msisdn": phone_number}

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"