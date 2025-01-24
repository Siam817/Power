import requests

def send_request(phone_number):
    url = "https://app.mmhf.jslglobal.co/api/v1/send-otp"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0"
    }
    data = {
        "phone": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise error for HTTP error responses
        return response.text  # Return the API response
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"