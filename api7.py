import requests

def send_request(phone_number):
    url = "https://api.motionview.com.bd/api/send-otp-phone-signup"
    headers = {
        "Host": "api.motionview.com.bd",
        "content-length": "23",
        "content-type": "application/json"
    }
    data = {
        "phone": phone_number
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return the full response text
    except Exception as e:
        return str(e)  # Return error message if an exception occurs