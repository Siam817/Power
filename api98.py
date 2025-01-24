import requests

def send_request(phone_number):
    url = "https://accountnow.nblbd.com/api/otp-request"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "okhttp/4.2.0"
    }
    payload = {
        "mobile": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)       
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}