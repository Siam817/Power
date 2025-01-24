import requests

def send_request(phone_no):
    # API URL and headers
    url = "https://www.icliniq.com/mobileajax/docSignup4PersonalDet?&os_type=android"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "okhttp/3.14.9"
    }

    # JSON payload
    payload = {
        "username": "10201034567",
        "name": "123456",
        "gender": "1",
        "dob": "2004/10/13",
        "mobile": phone_no[1:],  # Remove the leading "0" from the phone number
        "ccode": "880",
        "email": "12345",
        "pwd": "12345678"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.text  # Return response text
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"