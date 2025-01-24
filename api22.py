import requests

def send_request(phone_number):
    token_url = "https://accounts.sheba.xyz/api/v1/accountkit/generate/token?app_id=8329815A6D1AE6DD"
    token_headers = {
        "Host": "accounts.sheba.xyz"
    }

    try:
        token_response = requests.get(token_url, headers=token_headers)
        token_data = token_response.json()

        if token_data.get("code") == 200 and "token" in token_data:
            token = token_data["token"]

            otp_url = "https://accountkit.sheba.xyz/api/shoot-otp"
            otp_headers = {
                "Host": "accountkit.sheba.xyz",
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/json"
            }
            payload = {
                "mobile": f"+88{phone_number}",
                "app_id": "8329815A6D1AE6DD",
                "api_token": token
            }

            otp_response = requests.post(otp_url, headers=otp_headers, json=payload)
            return otp_response.text
        else:
            return "Error: Failed to generate token"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"