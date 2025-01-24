import requests

def send_request(phone_number):
    url = "http://103.4.145.86:6005/api/v1/user/otp/send"
    headers = {
        "Authorization": "Bearer 2Comics4mh5ln64ron5t26kpvm3toBlog",
        "Content-Type": "application/json",
        "Host": "103.4.145.86:6005"
    }
    data = {
        "msisdn": phone_number,
        "operator": "robi",
        "secret_key": ""
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"