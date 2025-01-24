import requests

def send_request(phone_number):
    url = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"
    headers = {
        "Host": "api.ghoorilearning.com",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Referer": "https://ghoorilearning.com/"
    }
    data = {
        "mobile_no": phone_number
    }

    try:
        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"