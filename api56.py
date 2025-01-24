import requests

def send_request(phone_number):
    # API endpoint
    url = "https://shopapp.self-shopping.com/public/webpost?random=157614&webpost=1"

    # Headers
    headers = {
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryckrDTqHo7ZGnmnYA",
        "Origin": "https://www.self-shopping.com"
    }

    # Data payload
    data = f"""------WebKitFormBoundaryckrDTqHo7ZGnmnYA
Content-Disposition: form-data; name="sendotp"

{phone_number}
------WebKitFormBoundaryckrDTqHo7ZGnmnYA
Content-Disposition: form-data; name="token"

N0ZHTEYyRTFBNzNWTzNVKl8qUkdUSVVFUVZMREg0NklTVE45SjRSQlBKTlZWUFRDMkk0NUVRQ0ZTN0FaWktWWk9PSk8qXyo1NDUxNDZiNWI3ZTg5N2JhNzAyMWU0ZWY4YWYwMTg4Ng==
------WebKitFormBoundaryckrDTqHo7ZGnmnYA--"""

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}