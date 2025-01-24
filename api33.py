import requests

def send_request(phone_number):
    url = "https://bb-api.bohubrihi.com/public/activity/otp"
    headers = {
        "Content-Type": "application/json",
        "Host": "bb-api.bohubrihi.com"
    }
    data = {
        "phone": phone_number,
        "intent": "login"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"