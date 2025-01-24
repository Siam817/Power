import requests

def send_request(phone_number):
    # Endpoint URL for registration
    register_url = "https://admin.beautybooth.com.bd/api/v2/auth/register"

    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://beautybooth.com.bd",
    }

    # Payload
    register_data = {
        "value": phone_number,
        "type": "phone"
    }

    try:
        # Sending POST request for registration
        response = requests.post(register_url, headers=headers, json=register_data)
        return response.json()  # Return JSON response
    except Exception as e:
        return {"error": str(e)}

def send_request(phone_number):
    # Endpoint URL for forget password request
    forget_url = "https://admin.beautybooth.com.bd/api/v2/auth/password/forget_request"

    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
    }

    # Payload
    forget_data = {
        "value": phone_number
    }

    try:
        # Sending POST request for forget password
        response = requests.post(forget_url, headers=headers, json=forget_data)
        return response.json()  # Return JSON response
    except Exception as e:
        return {"error": str(e)}