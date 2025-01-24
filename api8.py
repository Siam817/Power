import requests

def send_request(phone_number):
    url = f"https://scs.robi.com.bd/api/send-otp?mobile_no={phone_number}"

    try:
        # Send the GET request to the API
        response = requests.get(url)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"