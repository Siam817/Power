import requests

def send_request(phone_number):
    url = "https://api.gorillamove.com/api/v1/core/account/phone_login"
    headers = {
        "Host": "api.gorillamove.com",
        "Content-Type": "application/json",
        "Origin": "https://www.gorillamove.com",
    }
    data = {
        "phone_number": phone_number,
        "step": 1,
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.text  # Full response text return korche
    except Exception as e:
        return str(e)  # Error message return korche