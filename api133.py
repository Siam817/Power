import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://nxpay1.dutchbanglabank.com/user/register"
    
    # Headers
    headers = {
        "X-KM-User-AspId": "5678",
        "X-KM-Accept-language": "en",
        "X-KM-OS-SERVICE-TYPE": "GMS",
        "X-KM-User-Agent": "ANDROID/100046615",
        "Content-Type": "application/json",
        "Content-Length": "276",
        "Host": "nxpay1.dutchbanglabank.com",
        "User-Agent": "okhttp/4.9.3"
    }
    
    data = {
        "aspId": "5678",
        "dateOfBirth": None,
        "email": None,
        "gender": None,
        "locale": "EN",
        "mnoName": "LGU Plus",
        "msisdn": phone_number,
        "name": None,
        "nationality": None,
        "paymentPin": None,
        "registrationUserId": phone_number,
        "tcidList": [50],
        "telcoId": "GP",
        "verificationData": None,
        "walletPin": None
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}