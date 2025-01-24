import requests

def send_request(phone_number):
    url = "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en"
    headers = {
        "Host": "api.deeptoplay.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://www.deeptoplay.com"
    }
    data = {
        "number": f"+88{phone_number}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}