import requests

def send_request(phone_number):
    url = "https://softmaxmanager.xyz/api/v1/user/request/otp/"
    headers = {
        "user-agent": "Dart/3.2 (dart:io)",
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
        "authorization": "Basic c29zOjI3TTMjYTRz",
    }
    payload = {
        "phone_number": f"+88{phone_number}",
        "app_signature": "Fu89B+dY9dz",
        "location": "Null now",
        "device_name": "",
        "device_id": "TKQ1.221114.001",
        "android_version": "13",
        "app_version": "",
        "ram": "",
        "rom": ""
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}