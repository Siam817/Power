import requests

def send_request(phone_number):
    url = "https://userapi.fairbet91.com/api/RegisterUser/GenerateOTPV2"
    params = {
        "Mobile": phone_number,
        "SiteCode": "WBJ"
    }
    headers = {
        "Origin": "https://winbaji.com"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}