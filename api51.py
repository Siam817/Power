import requests

def send_request(phone_number):
    # API URL and headers
    url = "https://web.tallykhata.com/api/auth/init"
    headers = {
        "Authorization": "Basic c3luY191c2VyOlQhQjdZI0E5Jm48Y3M3QGM=",
        "api-version": "1.0",
        "app-version-code": "165",
        "Content-Type": "application/json",
        "Host": "web.tallykhata.com",
        "User-Agent": "okhttp/4.9.2"
    }

    # JSON payload
    payload = {
        "app_version_number": 165,
        "bp_code": "",
        "device_id": "5cd4397b-9b30-4604-91a3-e39cbf126d7e",
        "mobile": phone_number,
        "request_type": "LOGIN"
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}