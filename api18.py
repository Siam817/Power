import requests

def send_request(phone_number):
    url = f"https://api.medeasy.health/api/send-otp/+88{phone_number}/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    try:
        # Send GET request
        response = requests.get(url, headers=headers)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"