import requests

def send_request(phone_number):
    url = "https://dev.api.relaxy.com.bd/api/v1/otp/send"
    
    headers = {
        "User-Agent": "Dart/2.19 (dart:io)",
        "Content-Type": "application/json",
        "x-api-key": "6yjOGvakSbHjA64NGqo7m25TBC4WX8BauAXEP3dX"
    }
    
    # Replacing the phone number dynamically
    data = {
        "phoneNumber": f"+88{phone_number}",
        "appSignature": "appSignature"
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        
        # Returning the response text
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": sr(e)}