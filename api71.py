import requests

def send_request(phone_number):
    # API Endpoint
    url = "https://asia-south1-share-c8bbf.cloudfunctions.net/signUpPhoneCheck"

    # Request Headers
    headers = {
        "Firebase-Instance-ID-Token": "dholwtNAQlC9ZXBalwa_sa:APA91bGZ4D6we7LMhVcsPDcOVV4RB1ZF9bH4_lpBOcmkljauIxa4fv_3X2zFLAusZEpEW8OdBtDxK6fq6k4vqMna1F5pE2ZmQaG3l2_ycTUlnw6XOqLlZZQ",
        "Content-Type": "application/json",
        "Host": "asia-south1-share-c8bbf.cloudfunctions.net",
        "User-Agent": "okhttp/3.14.9"
    }

    # Request Payload
    data = {
        "data": {
            "userHashKey": "3F4518827F757D23D12F6CE8B8D5BFE5",
            "method": "init",
            "apiMd5": "41a84f1bd4b800c9e774ac3932635fbd",
            "phone": phone_number,
            "phoneEn": "ED37DA69D0BA5209F3FC21F45548EF1C",
            "deviceId": "9eb5fa822a01b1ed"
        }
    }

    try:
        # Send the POST Request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json()  # Parse and return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}