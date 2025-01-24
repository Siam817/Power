import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://admin.qualityfoods.com.bd/api/auth/check-phone"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Payload
    data = {
        "phone": phone_number,
        "is_sign_in": 0,
        "login_type": "phone"
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}