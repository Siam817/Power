import requests

def send_request(phone_no):
    # API URL and headers
    url = "https://ibanking.uttarabank-bd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "okhttp/3.14.9",
        "Connection": "Keep-Alive"
    }

    # JSON payload
    payload = {
        "AccessToken": "",
        "TrackingNo": "",
        "mobileNo": phone_no,
        "otpSms": "",
        "product_id": "111",
        "requestChannel": "MOB",
        "trackingStatus": 5
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}