import requests

def send_request(phone_number):
    url = "https://backend.bppshop.com.bd/api/v1/auth/send"
    headers = {
        "Host": "backend.bppshop.com.bd",
        "Content-Type": "application/json",
    }
    payload = {
        "phone": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"