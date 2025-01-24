import requests

def send_request(phone_number):
    url = 'https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'okhttp/4.10.0'
    }

    payload = {
        "AccessToken": "",
        "TrackingNo": "",
        "mobileNo": phone_number,
        "otpSms": "",
        "product_id": "131",
        "requestChannel": "MOB",
        "trackingStatus": 5
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.text
    except Exception as e:
        return str(e)