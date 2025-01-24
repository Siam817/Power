import requests

def send_request(phone_number):
    # API endpoint
    url = "https://api.mkiddo.com/api/V2/send-otp"

    # Headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Data payload
    data = f'app_signature=DMSfFDCvin4&app_name=mKiddo_v%253A2.6.4&source=app&msisdn={phone_number}'

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}