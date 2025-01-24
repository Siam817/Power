import requests

def send_request(phone_number):
    # Step 1: Get Access Token
    token_url = "https://keeron.com/api/identity/v100/identity/token"
    token_headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://keeron.com",
        "Accept-Language": "en"
    }
    token_data = {
        "grant_type": "authenticate_site"
    }

    try:
        # POST request to get access token
        token_response = requests.post(token_url, headers=token_headers, data=token_data)
        token_response.raise_for_status()  # Raise error if response code is not 200
        token_json = token_response.json()
        access_token = token_json.get("access_token")

        if not access_token:
            return {"error": "Access token not found in the response."}
    except Exception as e:
        return {"error": f"Failed to get access token: {str(e)}"}

    # Step 2: Validate Mobile
    validate_url = "https://keeron.com/api/business-keeron/auth/validate-mobile"
    validate_headers = {
        "Host": "keeron.com",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://keeron.com/",
        "Cookie": f"keeron.com={access_token}"
    }
    validate_params = {
        "mobile": f"88{phone_number}"
    }

    try:
        # GET request to validate mobile
        validate_response = requests.get(validate_url, headers=validate_headers, params=validate_params)
        validate_response.raise_for_status()  # Raise error if response code is not 200
        return validate_response.json()
    except Exception as e:
        return {"error": f"Failed to validate mobile: {str(e)}"}