import requests

def send_request(phone_number):
    
    url = "https://www.practiceclub.net/api/register"

    headers = {
        "Host": "www.practiceclub.net",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/4.9.0"
    }

    data = {
        "contact_no": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}