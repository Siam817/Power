import requests

def send_request(phone_number):
    url = f"https://alglimited.com/api/v1/otp-sms-send/{phone_number}"
    headers = {
        "Accept": "application/json",
        "Host": "alglimited.com"
    }

    try:
        # Send GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}