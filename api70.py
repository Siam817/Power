import requests

def send_request(phone_number):
    # Define the endpoint
    url = "https://identity01.qpaybd.com.bd/api/v1/verification/phone"

    # Define the payload
    data = {
    "Id": phone_number,  # Replace with the desired phone number
    "DeviceId": "dCCsO6E3Tw62Wuu28mPXOX:APA91bFgSqIneBZ1aV1aizEpWKu3C05TX6o9_J4Q4buv2LndDD3nKPb60xWMqiZA2rpku1ZoPklFL1dCi-vdhKr7Ti1lywH1fKIOL9qniTZHXroE7aPOHXM",
}

    # Define the headers
    headers = {
        "user-agent": "Dart/3.2 (dart:io)",
    }

    try:
        # Send the POST request
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}