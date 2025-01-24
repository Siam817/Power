import requests

def send_request(phone_number):
    url = "https://new.mojaru.com/api/student/login-registration"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = f"mobile_or_email={phone_number}&app_hash_key=hi&app_mode=RELEASE"
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, data=data)
        
        # Return the response text
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}