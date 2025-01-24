import requests

def send_request(phone_number):
    url = "https://smartukil.com/api/send-verification-code"
    headers = {
        "Host": "smartukil.com",
        "authorization": "ergjvbner234erv%^&hjb23QQ!FL*qpdjfweufhjvYUH%^&hj367^&*bedvhjb%^&RhjkbwerfIHVyIy!6XC3E",
        "content-type": "application/x-www-form-urlencoded"
    }
    data = {
        "phone": phone_number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}