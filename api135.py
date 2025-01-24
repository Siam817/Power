import requests

def send_request(phone_number):
    url = "https://distribution.hishabee.business/api/app/v1/auth/number-check"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mobile_number": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"