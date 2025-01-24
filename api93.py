import requests

def send_request(phone_number):
    url = "https://backend.karobarapp.com/auth/phone-login/"
    
    headers = {
        "user-agent": "Dart/3.4 (dart:io)",
        "content-type": "application/json"
    }
    
    payload = {
        "phone_number": phone_number[1:],
        "os": "Android",
        "country": "bangladesh"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}