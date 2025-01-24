import requests

def send_request(phone_number):
    url = "https://api.munchies.com.bd/parse/functions/generateOtp"
    headers = {
        "x-parse-application-id": "food",
        "Content-Type": "application/json"
    }
    data = {
        "phone": phone_number
    }

    try:
        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"