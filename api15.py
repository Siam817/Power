import requests

def send_request(phone_number):
    url = "https://boichitro.com.bd/api/v1/auth/send-signup-otp/"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "phone": f"+88{phone_number}",  # Format the phone number with country code
        "app_key": ""  # Leave empty as specified
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"