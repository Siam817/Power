import requests

def send_request(phone_number):
    
    url = "http://apps.babuland.org/bblapi/apiv2/apiv5/bbl_api_user_otp"

    headers = {
        "User-Agent": "Dart/2.19 (dart:io)",
        "Host": "apps.babuland.org",
        "mobileno": f"+88{phone_number}",
        "otpcode": "111135",
        "branchid": "6",
        "Content-Length": "0"
    }

    try:
        response = requests.post(url, headers=headers)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}