import requests

def send_request(phone_number):
    url = "https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp"
    headers = {"Content-Type": "application/json"}
    
    # Prepare data dynamically with phone number
    data = {
        "deviceId": "7dtdhid45c0f0901",
        "deviceInfo": {
            "deviceInfoSignature": "D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA",
            "deviceId": "7d8b0agi0g0f0901",
            "firebaseDeviceToken": "",
            "manufacturer": "MI",
            "modelName": "NOTE 10",
            "osFirmWireBuild": "",
            "osName": "Android",
            "osVersion": "10",
            "rootDevice": 0
        },
        "operator": "88",
        "walletNumber": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"