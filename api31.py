import requests

def send_request(phone_number):
    url = f"https://m-backend.wafilife.com/wp-json/wc/v2/send-otp"
    params = {
        "p": f"88{phone_number}",
        "consumer_key": "ck_e8c5b4a69729dd913dce8be03d7878531f6511ff",
        "consumer_secret": "cs_f866e5c6543065daa272504c2eea71044579cff3"
    }

    try:
        # Send GET request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"