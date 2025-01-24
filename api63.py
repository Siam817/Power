import requests
import random

def send_request(phone_number):
    # API endpoint
    url = "https://abclit.com/api/sendOTP"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Auto-generate 4-digit OTP
    otp_code = random.randint(1000, 9999)

    # Data payload
    data = f'{{"recipientNo":"{phone_number}","code":{otp_code}}}'

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for HTTP request errors
        return {"response": response.text, "generated_otp": otp_code}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}