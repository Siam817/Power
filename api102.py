import requests

def send_request(phone_number):
    url = "https://api.v2.medico.bio/patient/passwordless-login"
    headers = {
        "Host": "api.v2.medico.bio",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://medico.bio"
    }
    payload = {
        "phoneNumber": phone_number,
        "deviceId": phone_number,
        "channel": "web",
        "userType": "patient",
        "type": "newUser"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}