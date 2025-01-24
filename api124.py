import requests

def send_request(phone_number):
    # API Endpoint
    url = "https://healthway.com.bd/account/api/send/otp/"

    # Headers
    headers = {
        "Host": "healthway.com.bd",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://healthway.com.bd",
    }

    # Data
    data = {
        "username": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}