import requests

def send_request(phone_number):
    url = "https://api.onefish.app/api/auth/user/sendotp"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "phone": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"