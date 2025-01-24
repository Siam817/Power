import requests

def send_request(phone_number):
    url = "https://sasthyaseba.com/register/q-data.json?qaction=id_d401qvL6ESs"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json, charset=UTF-8",
        "Tracestate": "4711699@nr=0-1-4711699-538634595-248b554734804cdd----1736920057854",
        "Origin": "https://sasthyaseba.com"
    }
    data = {
        "type": "send-otp",
        "phone": f"+88 {phone_number}",
        "email": "",
        "name": "Rahat",
        "gender_id": 1
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}