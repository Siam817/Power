import requests

def send_request(phone_number):
    url = f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone_number}"
    headers = {
        "Host": "backoffice.ecourier.com.bd",
        "Connection": "keep-alive",
        "Origin": "https://ecourier.com.bd"
    }
    try:
        response = requests.get(url, headers=headers)
        return response.text  # Return the full response text
    except Exception as e:
        return str(e)  # Return error message if an exception occurs