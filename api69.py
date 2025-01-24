import requests

def send_request(phone_number):
    # Base URL for both actions
    base_url = "https://www.emartwayskincare.com.bd"
    
    headers = {
        "user-agent": "Dart/2.19 (dart:io)",
        "Content-Type": "application/json"
    }

    # Signup request
    signup_url = f"{base_url}/api/v2/auth/signup"
    signup_data = {
        "name": "emartway",
        "email_or_phone": f"+88{phone_number}",
        "password": "1234567890",
        "password_confirmation": "1234567890",
        "register_by": "phone"
    }

    # Forgot password request
    forgot_password_url = f"{base_url}/api/v2/auth/password/forget_request"
    forgot_password_data = {
        "email_or_phone": f"+88{phone_number}",
        "send_code_by": "phone"
    }

    try:
        # Send POST request for signup
        signup_response = requests.post(signup_url, headers=headers, json=signup_data)
        signup_response.raise_for_status()  # Check for HTTP errors
        signup_result = signup_response.json()  # Parse JSON response

        # Send POST request for forgot password
        forgot_password_response = requests.post(forgot_password_url, headers=headers, json=forgot_password_data)
        forgot_password_response.raise_for_status()  # Check for HTTP errors
        forgot_password_result = forgot_password_response.json()  # Parse JSON response

        return signup_result, forgot_password_result  # Return both responses

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None