import requests

def send_request(phone_number):
    url = "https://api.bacbontutors.com/V2/student/pre-register"
    
    headers = {
        "Host": "api.bacbontutors.com",
        "Content-Type": "application/json"
    }
    
    data = {
        "name": "12345",
        "mobile_no": phone_number,
        "email": "",
        "referred_code": None,
        "app_signature": "BacBon Tutors"
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json()  # Parse response as JSON
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return error message
        return {"error": str(e)}