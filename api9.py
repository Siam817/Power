import requests

def send_request(phone_number):
    url = "https://www.hehe555888.com/wps/verification/sms/register"
    headers = {
        "language": "EN",
        "authorization": "",
        "merchant": "hehe555f3",
        "moduleid": "REGMOBVERF3",
        "user-agent": "Mozilla/5.0",
        "content-type": "application/json"
    }
    data = {
        "mobileNo": phone_number[-10:],  # Use the last 10 digits for mobileNo
        "countryDialingCode": "880"
    }

    try:
        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=data)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"