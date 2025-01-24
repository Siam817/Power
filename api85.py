import requests

def send_request(phone_number):
    url = "https://auth.acsfutureschool.com/api/v1/otp/send"
    headers = {
        "user-agent": "Mozilla/5.0",
        "content-type": "application/json"
    }
    payload = {
        "phone": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}