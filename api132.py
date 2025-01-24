import requests

def send_request(phone_number):
    url = "https://api.eat-z.com/auth/customer/app-connect"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "okhttp/4.12.0"
    }
    
    data = {
        "username": f"+88{phone_number}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}