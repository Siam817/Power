import requests

def send_request(phone_number):
    # API URL and headers
    url = "https://app.wearnsmile.com.bd/api/v1/1/ecom/auth/getCode"
    headers = {
        "Content-Type": "application/json"
    }
    
    # JSON payload
    payload = {
        "mobile": phone_number
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}