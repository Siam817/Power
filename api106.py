import requests

def send_request(phone_number):
    url = "https://ap.paymasterbd.net/login_registration/"
    
    headers = {
        "Host": "ap.paymasterbd.net",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/3.14.9"
    }
    
    data = {
        "phone_number": phone_number,
        "fcm_key": "",
        "device_id": "b5f0985eb84c4bfa",
        "sms_hash_code": "s2//QkN6BpW"
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, data=data)
        
        # Returning the response text
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": sr(e)}