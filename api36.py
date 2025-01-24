import requests

def send_request(phone_number):
    # Base URL for both actions
    base_url = "https://bibaho.ecombd.org"
    
    headers = {
        "Content-Type": "application/json"
    }

    # Signup request
    signup_url = f"{base_url}/signup"
    signup_data = {
        "name": "Chowa",
        "mobile": phone_number,
        "password": "Chowa@123",
        "accountFor": "Self",
        "accountType": "General",
        "androidId": "7991e6b06da542fe",
        "osName": "Android",
        "osBuildId": "QKQ1.190910.002 V12.5.3.0.QFGMIXM",
        "ipAddress": ""
    }

    # Forgot password request
    forgot_password_url = f"{base_url}/forgot-password"
    forgot_password_data = {
        "mobile": phone_number
    }

    # Send POST request for signup
    try:
        signup_response = requests.post(signup_url, headers=headers, json=signup_data)
        signup_response.raise_for_status()  # Raises HTTPError for bad responses
        signup_result = signup_response.text  # Save the response text

        # Send POST request for forgot password
        forgot_password_response = requests.post(forgot_password_url, headers=headers, json=forgot_password_data)
        forgot_password_response.raise_for_status()  # Raises HTTPError for bad responses
        forgot_password_result = forgot_password_response.text  # Save the response text

        return signup_result, forgot_password_result  # Return both responses

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None  # Return None in case of an error