import requests

def send_request(phone_number):
    # API endpoint
    url = "https://ecom.rangs.com.bd/send-otp-code"
    
    # Headers
    headers = {
        "Host": "ecom.rangs.com.bd",
        "authorization": "Bearer",  # Add the actual token if required
        "user-agent": "Mozilla/5.0",
        "content-type": "application/json",
        "origin": "https://shop.rangs.com.bd",
        "referer": "https://shop.rangs.com.bd/"
    }
    
    # Payload
    data = {
        "mobile": f"+88{phone_number}",
        "type": 1
    }
    
    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}