import requests

def send_request(phone_number):
    url = "https://badhan-api.stylezworld.net/api/otp/store"
    headers = {
        "app-access-token": "mWR+64IbKwxM2XCyJbMvUSCcc=",
        "Content-Type": "application/json",
        "User-Agent": "",
        "Authorization": "null",
        "Host": "badhan-api.stylezworld.net"
    }
    data = {
        "phone_number": phone_number,
        "registration_phone_number": phone_number,
        "auto_fill": "hiiii",
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return full response text
    except Exception as e:
        return str(e)  # Return error message if exception occurs