import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://expresshub.com.bd/User/CreateNewUser"

    # Headers
    headers = {
        "Host": "expresshub.com.bd",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://expresshub.com.bd"
    }

    # Data payload
    data = {
        "_UID": phone_number,
        "_UNAME": "0",
        "_MAIL": "0",
        "_PHONE": "0",
        "_PASS": "0",
        "_TYPE": "1"
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        return response.text  # Return response text
    except Exception as e:
        return str(e)