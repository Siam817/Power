import requests

def send_request(phone_number):
    url = "https://api.bepari.app/bestfreshfarm/api/V1.4/access-control/user/registerOtp"

    headers = {
        "Host": "api.bepari.app",
        "Content-Type": "application/json",
        "Origin": "https://www.bestfreshfarm.com"
    }

    data = {
        "client_id": 4,
        "client_secret": "zCzOixaOJ4JywQr1VsowGZhCaEbZ49WLxweNBgPK",
        "mobile_no": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Return server response as JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}