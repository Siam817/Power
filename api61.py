import requests

def send_request(phone_number):
    # API endpoint
    url = "https://api.osudkini.com/api/otp/generate-otp"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }

    # JSON payload
    data = {
        "phoneNo": phone_number
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}