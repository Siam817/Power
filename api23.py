import requests

def send_request(phone_number):
    url = "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en"
    headers = {
        "Authorization": "",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://www.chorki.com",
    }
    payload = {"number": f"+88{phone_number}"}

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return API response
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"