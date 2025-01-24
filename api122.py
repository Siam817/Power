import requests

def send_request(phone_number):
    # Endpoint URL
    url = f"https://shop.pharmaid-rx.com/api/sendSMSRegistration?mobileNumber={phone_number}"

    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Host": "shop.pharmaid-rx.com"
    }

    try:
        response = requests.get(url, headers=headers)
        return response.text
    except Exception as e:
        return {"error": str(e)}