import requests

def send_request(phone_number):
    # API endpoint
    url = "https://admin.wholesaleplus.com.bd/api/send-otp/"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Payload
    payload = {
        "email": phone_number,
        "regi": True
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Return the server response as JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}