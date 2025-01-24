import requests

def send_request(phone_number):
    url = "https://api.hurraayy.com/api/v1/open/login/otp-send"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "phone": phone_number,
        "code": "hlw"
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": sr(e)}