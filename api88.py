import requests

def send_request(phone_number):
    url = "https://meyeghor.com/wp-json/digits/v1/send_otp"
    headers = {
        "User-Agent": "Dart/3.2 (dart:io)",
        "Accept": "application/json",
        "Timedifference": "360",
        "Authorization": "Basic Y2tfNzk3MzQ0NzljZWUxZTU2Y2M1MjBkODczOTkxZGRhYjE5ZTMwYzQyMzpjc18xMmE5ODFkODYzMmE1NDMyMzMzNmY0YWNmNWVkNjYxNmQzM2JkNTU2",
        "X-API-Version": "1.1",
    }
    data = {
        "countrycode": "+880",
        "mobileNo": phone_number,
        "type": "register",
        "email": f"{phone_number}@gmail.com",
    }
    
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}