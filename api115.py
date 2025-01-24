import requests

def send_request(phone_number):
    # Endpoint URL
    url = f"https://www.uzanvati.com/user/otp?phone={phone_number}"

    # Headers
    headers = {
        "Host": "www.uzanvati.com",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        return response.text
    except Exception as e:
        return str(e)