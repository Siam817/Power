import requests

def send_request(phone_number):
    url = "https://api.osudpotro.com/api/v1/users/send_otp"
    
    headers = {
        "Host": "api.osudpotro.com",
        "Content-Type": "application/json",
        "Origin": "https://osudpotro.com"
    }
    
    data = {
        "mobile": f"+88-{phone_number}",
        "deviceToken": "web",
        "language": "en",
        "os": "web"
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json()  # Parse response as JSON
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return error message
        return {"error": str(e)}