import requests

def send_request(phone_number):
    url = "https://orderwalabd.com/backend-development/public/api/retailer/create-otp"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "phone": phone_number
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        
        # Returning the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": sr(e)}