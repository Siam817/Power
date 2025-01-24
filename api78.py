import requests

def send_request(phone_number):
    # API endpoint
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
    
    # Headers
    headers = {
        "Host": "prod-api.viewlift.com",
        "user-agent": "Mozilla/5.0",
        "content-type": "application/json",
        "x-api-key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef",
        "origin": "https://www.hoichoi.tv"
    }
    
    # Payload
    data = {
        "phoneNumber": f"+88{phone_number}",
        "requestType": "send",
        "whatsappConsent": False
    }
    
    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}