import requests

def send_request(phone_number):
    url = "https://www.amiprobashi.com/api/v7/en/auth/send-otp"

    headers = {
        "android-app-version": "4.5.0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "okhttp/4.10.0",
    }

    data = {
        "device_type": "1",
        "username": f"+88{phone_number}",
        "for": "1",
        "type": "1",
        "bd_number": "1",
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for HTTP errors
        return response.text  # Return the server's response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}