import requests

def send_request(phone_number):
    # API endpoint
    url = "https://api.chardike.com/api/otp/send"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://chardike.com"
    }

    # Data payload
    data = {
        "phone": phone_number,
        "otp_type": "login"
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.text  # Return the server response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}