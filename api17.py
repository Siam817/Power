import requests

def send_request(phone_number):
    url = "https://bimafy.com/api/v2/send-otp-code"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "name": "",
        "otp_code": "",
        "mobile": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"