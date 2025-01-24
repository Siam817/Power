import requests

def send_request(phone_number):
    url = "https://core.easy.com.bd/api/v1/registration"
    headers = {
        "Host": "core.easy.com.bd",
        "Connection": "keep-alive",
        "lang": "en",
        "device-key": "48b1f7061f48c950090220f62128b2c3",
        "Content-Type": "application/json"
    }
    data = {
        "social_login_id": "",
        "name": "Rahat",
        "email": "chowa@gmail.com",
        "mobile": phone_number,
        "password": "123456",
        "password_confirmation": "123456",
        "device_key": "48b1f7061f48c950090220f62128b2c3"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return the full response text
    except Exception as e:
        return str(e)  # Return error message if an exception occurs