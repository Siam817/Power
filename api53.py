import requests

def send_request(phone_number):
    # API URL and headers
    url = "https://eaccount.bdbl.com.bd:31091/api/mobile/onboarding/CustomerMobileOTPGenerate"
    headers = {
        "content-type": "application/json",
        "isauthrequired": "false",
        "tokenvalidateid": ""
    }
    
    # JSON payload
    payload = {
        "BusinessData": {
            "MobileNumber": f"+88{phone_number}"
        }
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return response.json()  # Return the parsed JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}