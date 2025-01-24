import requests

def send_request(phone_number):
    url = "https://acurebd.com/users/ajax_otpsms"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    # Construct the data payload with the phone number and timestamp
    data = f"mobile={phone_number}&vtm=28%2F11%2F2023%2C%2022%3A21%3A39"  # Example timestamp

    try:
        # Send the POST request
        response = requests.post(url, headers=headers, data=data)
        # Return the response text
        return response
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}