import requests

def send_request(phone_number):
    url = "https://api.klassy.com.bd/api/v2/public/user/register/send/otp"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    # Request body with the phone number
    data = {
        "phone": phone_number
    }

    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return the server response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}