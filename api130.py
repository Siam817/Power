import requests

def send_request(phone_number):
    url = "https://edge.ali2bd.com/api/consumer/v1/auth/login"
    
    # Headers
    headers = {
        "Host": "edge.ali2bd.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Referer": "https://mobile.ali2bd.com/"
    }
    
    # Payload
    data = {
        "username": f"+88{phone_number}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"