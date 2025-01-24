import requests

def send_request(phone_number):
    url = "https://api.ilyn.global/auth/signup"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarylKIx6ZhornTyt7tA"
    }

    # Manually crafting the multipart form data as a string
    data = (
        "------WebKitFormBoundarylKIx6ZhornTyt7tA\r\n"
        "Content-Disposition: form-data; name=\"phone\"\r\n\r\n"
        f'{{"code":"BD","number":"{phone_number}"}}\r\n'
        "------WebKitFormBoundarylKIx6ZhornTyt7tA\r\n"
        "Content-Disposition: form-data; name=\"provider\"\r\n\r\n"
        "sms\r\n"
        "------WebKitFormBoundarylKIx6ZhornTyt7tA--"
    )

    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}