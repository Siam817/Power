import requests

def send_request(phone_number):

    url = "https://moveonbd.com/api/v1/customer/auth/phone/request-otp"
    
    headers = {
        "Host": "moveonbd.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Referer": "https://moveon.com.bd/"
    }
    
    data = {
        "phone": phone_number
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}