import requests

def send_request(phone_number):
    url = f"http://202.51.186.182:33262/api/v1/generate-otp?phone={phone_number}"
    headers = {
        "User-Agent": "Dart/2.19 (dart:io)",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers)       
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}