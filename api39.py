import requests

def send_request(phone_number):
    url = "https://admissionprostuti.com/api/app/otp-sent?fromApp=true"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # Format the data with the dynamic phone number
    data = f"mobile={phone_number}"

    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"