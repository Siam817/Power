import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://api.lefabrebd.com/api/v1/customer/register"

    # Headers
    headers = {
        "Host": "api.lefabrebd.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://www.lefabrebd.com"
    }

    # JSON Payload
    data = {
        "name": "Chowa",
        "phone": phone_number,
        "password": "123456"
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return response text
    except Exception as e:
        return str(e)