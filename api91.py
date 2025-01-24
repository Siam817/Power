import requests

def send_request(phone_number):
    url = f"https://apon.ibos.io/apon/partner/Registration/OTPGenerate?PhoneNumber={phone_number}&Typeid=1"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers)
        
        # Return the response text
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}