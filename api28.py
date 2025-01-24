import requests

def send_request(phone_number):
    url = "https://www.letsbett.com/wps/verification/sms/register"
    headers = {
        "Host": "www.letsbett.com",
        "Language": "EN",
        "Merchant": "letsbetf2",
        "ModuleID": "REGMOBVERF3",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://www.letsbett.com"
    }
    payload = {
        "mobileNo": phone_number,
        "countryDialingCode": "880"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"