import requests

def send_request(phone_number):
    url = "https://api.shikho.com/auth/v2/send/sms"
    headers = {
        "Accept": "application/json,application/json",
        "Build-Version": "(450) 4.5.0",
        "Content-Type": "application/json",
        "Host": "api.shikho.com"
    }
    data = {
        "adjust_id": "",
        "google_ads_id": "",
        "auth_type": "signup",
        "phone": phone_number,
        "type": "student",
        "vendor": "shikho"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"