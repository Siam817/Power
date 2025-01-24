import requests

def send_request(phone_number):
    url = "https://api.bdtickets.com:20100/v1/auth"
    headers = {
        "Host": "api.bdtickets.com:20100",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://bdtickets.com"
    }
    data = {
        "createUserCheck": True,
        "phoneNumber": f"+88{phone_number}",
        "applicationChannel": "WEB_APP"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}