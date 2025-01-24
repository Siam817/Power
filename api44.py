import requests

def send_request(phone_number):
    url = "https://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmail"
    
    headers = {
        "Authorization": "bearer 3__k_BR7BwLTdd8JK1gKg1a5ADpIShfv0pbzq5gNok7UZMaYxe0xWd_JEbd84CqQP1KHKWNpLkdQdEsENo9nf2OKl2GKzkfIKoy8vLGevphA8-DWDl0YXfdUhFaAuRz3R8RqHKo2tx0Z2BPHAMjkldYgVQJFg2LWoiZLi0NkhVqwfrIFPGGVmmjDxowdkm2TkkV-C5iF2RE_bPensavjXtYCUn5sOg53am3wSUShtJ5CjeE5",
        "accept-language": "en",
        "productCode": "FS",
        "Content-Type": "application/json"
    }

    payload = {
        "ekycApplicationData": {
            "emailId": "",
            "id": 0,
            "mobileNumber": phone_number,
            "productCode": "FS"
        },
        "channel": "ANDROID_APP",
        "deviceName": "",
        "deviceNumber": "",
        "hardwareSignature": "",
        "mobileAppVersion": "4.2.1_RELEASE",
        "mobileAppVersionCode": 45,
        "productCode": "FS",
        "requestId": "",
        "sessionToken": ""
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json()  # Parse response as JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}