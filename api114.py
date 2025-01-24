import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://e-unionint.com/rides/api/otp.php"

    # Headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/4.10.0"
    }

    # Payload
    data = {
        "mobile": phone_number
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        return response.text
    except Exception as e:
        return str(e)