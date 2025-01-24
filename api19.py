import requests

def send_request(phone_number):
    url = "https://qfood.com.bd/api/send-otp"
    headers = {
        "Host": "qfood.com.bd",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://qfood.com.bd"
    }
    payload = {
        "mobileNumber": f"+88{phone_number}"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"