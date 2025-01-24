import requests

def send_request(phone_number):
    url = "https://api.picky.com.bd/api/user/v2/customer/send-otp-for-login"
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "phone": f"+88{phone_number}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}