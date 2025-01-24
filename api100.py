import requests

def send_request(phone_number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone_number}"
    headers = {
        "Host": "bikroy.com",
        "Application-Name": "web",
        "Accept-Language": "bn",
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}