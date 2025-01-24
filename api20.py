import requests

def send_request(phone_number):
    url = "https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber"
    headers = {
        "Host": "us-central1-doctime-465c7.cloudfunctions.net",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://doctime.com.bd",
    }
    payload = {
        "data": {
            "country_calling_code": "88",
            "contact_no": phone_number,
            "headers": {"PlatForm": "Web"}
        }
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"