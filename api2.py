import requests

def send_request(phone_number):
    url = "https://app.kireibd.com/api/v2/send-login-otp"
    headers = {
        "user-agent": "Dart/3.3 (dart:io)",
        "content-type": "application/json; charset=utf-8",
        "accept": "*/*",
        "accept-encoding": "gzip",
        "host": "app.kireibd.com",
    }
    data = {"email": phone_number}  # Phone number as email in the API request body
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.text  # Return full response text
    except Exception as e:
        return str(e)  # Return error message if exception occurs