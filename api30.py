import requests

def send_request(phone_number):
    url = "https://doctorlivebd.com/api/patient/auth/otpsend"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = f"country_code=880&mobile={phone_number[1:]}"

    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"