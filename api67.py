import requests

def send_request(phone_number):
    # API endpoint
    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"

    # Headers
    headers = {
        "User-Agent": "Dart/2.12 (dart:io)",
        "x-api-key": "gYsiNSVBDuCt8yMUXpF06iQ1eDrMGv6G",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "developer.quizgiri.xyz"
    }

    # Data payload
    data = {
        "phone": phone_number[1:],  # Remove leading '0' from the phone number
        "country_code": "+880",
        "fcm_token": "cCeo3JLSRF2J62oZiCYXD-:APA91bH1Ds1yvx82qEOD1FAQQZ2hWs2a9rjzSKLcRPRMfSBquopudh02J-LS_VU2nlUUWL-TTkSuKsGMDnQIr9JWMbFr_LYSjlgLtASMEq4fXojujAhWa44"
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()  # Return server response in JSON format
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}