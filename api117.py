import requests

def send_request(phone_number):
    
    url = "https://hhcjmpjdld.execute-api.ap-southeast-1.amazonaws.com/prod/accounts/user/continue_with_phone"

    headers = {
        "Host": "hhcjmpjdld.execute-api.ap-southeast-1.amazonaws.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://www.amardoctor.health"
    }

    data = {
        "phone": phone_number,
        "user_type": "patient",
        "send_msg": True
    }

    try:       
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}