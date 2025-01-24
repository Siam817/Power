import requests

def send_request(phone_number):
    url = "https://agricare.global/api/login/generate-otp"
    
    headers = {
        "Host": "agricare.global",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://agricare.global"
    }
    
    data = {
        "phone": phone_number
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        
        # Returning the response text
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": sr(e)}