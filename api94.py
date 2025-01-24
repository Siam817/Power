import requests

def send_request(phone_number):
    url = "http://mmbl-eaccount.modhumotibank.net/api/otp-request"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "mobile": phone_number
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}