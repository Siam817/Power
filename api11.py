import requests

def send_request(phone_number):
    url = f"https://web-api.binge.buzz/api/v3/otp/send/+88{phone_number}"
    headers = {
        "Device-Type": "web",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        # Send the GET request to the API
        response = requests.get(url, headers=headers)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"