import requests

def send_request(phone_number):
    url = "http://api.myguardianbd.com/api/requestOtp"
    
    headers = {
        "Authorization": "Bearer Y0iZuYIK0lad8IeVdv6UWWlZ1sJPzIHqZZoA8yrHDzzKrSW6porY5zVz3RwM6VifLrf2XfirGsVzcAhlOCLLXftlIJvxAmRdW8c0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = f"new=1&device_id=ec352e5211d128ea&mobile={phone_number}"
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}