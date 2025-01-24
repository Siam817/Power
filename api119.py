import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://fundesh.com.bd/api/auth/generateOTP"

    # Headers
    headers = {
        "Host": "fundesh.com.bd",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://fundesh.com.bd"
    }

    # JSON Payload
    data = {
        "msisdn": phone_number[1:]  # Removing the first digit (country code prefix)
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return response text
    except Exception as e:
        return str(e)