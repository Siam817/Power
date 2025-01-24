import requests

def send_request(phone_number):
    url = "https://htmind.live/api/user/otp-request"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "phone": f"880{phone_number}",  # Dynamically set the phone number
        "secret_key": ""  # Secret key field kept empty as per the original script
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"