import requests

def send_request(phone_number):
    # API endpoint
    url = "https://meenabazardev.com/api/mobile/front/send/otp"

    # Payload with dynamic phone number
    data = {
        "CellPhone": phone_number,
        "type": "login"
    }

    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        # Send POST request
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text  # Return the response body
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}