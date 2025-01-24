import requests

def send_request(phone_number):
    url = "https://api.jeeto.online/user/phone-number"

    headers = {
        "user-agent": "Dart/3.0 (dart:io)",
        "content-type": "application/json"
    }

    payload = {
        "phone_number": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.text
    except Exception as e:
        return str(e)