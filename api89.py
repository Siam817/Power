import requests

def send_request(phone_number):
    url = "https://app.deshal.net/api/auth/login"
    headers = {"Content-Type": "application/json"}
    data = {"phone": phone_number}

    try:
        # Send the POST request
        response = requests.post(url, headers=headers, json=data)
        # Return the response text
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}