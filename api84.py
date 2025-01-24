import requests

def send_request(phone_number):
    url = "https://walton-amar-awaz-prod.com/api/user/signup"
    headers = {
        "accept": "application/json",
        "version-code": "1.4.7",
        "authorization": "Bearer",
        "content-type": "application/json",
        "user-agent": "okhttp/4.7.2"
    }
    payload = {
        "email": f"{phone_number}@example.com",
        "fbId": "",
        "fullName": "User",
        "gId": "",
        "phone": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}