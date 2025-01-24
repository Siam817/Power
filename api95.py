import requests

def send_request(phone_number):
    url = "https://shl.com.bd/api/appapi/sendOTP"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = f"number={phone_number}"  # Dynamically insert the phone number

    try:
        response = requests.post(url, headers=headers, data=data)
        
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}