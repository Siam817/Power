import requests

def send_request(phone_number):
    # API endpoint
    url = "https://coreapi.shadhinmusic.com/api/v5/otp/OtpRobiReq"

    # Headers
    headers = {
        "Host": "coreapi.shadhinmusic.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
    }

    # JSON payload
    data = {
        "msisdn": f"88{phone_number}",
        "shortcode": 16235,
        "servicename": "Shadhin Music"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}