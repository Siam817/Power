import requests

def send_request(phone_number):
    url = "https://api.rangsmotors.com/"
    params = {
        "file_name": "send_otp",
        "u_num": phone_number
    }
    headers = {
        "Origin": "https://www.garimela.com"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}