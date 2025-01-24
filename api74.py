import requests

def send_request(phone_number):
    # API endpoint
    url = "https://training.gov.bd/backoffice/api/user/sendOtp"
    
    # Headers
    headers = {
        "Host": "training.gov.bd",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    
    # Payload
    data = {
        "mobile": phone_number
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}