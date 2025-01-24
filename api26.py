import requests

def send_request(phone_number):
    url = "https://www.v88bd.com/en/api/sendOtp"
    headers = {
        "Host": "www.v88bd.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://www.v88bd.com",
    }
    payload = {
        "phone": phone_number,
        "otpMethod": "register",
        "fingerprint": "0593256e7c6c6d969b479d6f10e5bf4b"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"