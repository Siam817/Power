import requests

def send_request(phone_number):
    url = f"https://chinaonlinebd.com/api/login/getOtp?phone={phone_number}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Token": "45601f3d391886fcec5f5a3f26780f21"
    }

    try:
        response = requests.get(url, headers=headers)
        
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}