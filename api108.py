import requests

def send_request(phone_number):
    url = "https://customerapp-gateway-ktor.prod.porter.ae/onboarding/customer/signup"
    
    headers = {
        "Host": "customerapp-gateway-ktor.prod.porter.ae",
        "country": "bd",
        "preferred-languages": '{"app_language":"en"}',
        "brand": "porter",
        "source": "android",
        "version-name": "6.7.0",
        "custom-app-version-code": "410",
        "client-request-uuid": "88c7743e-d714-4735-ad05-339e43cf8e73",
        "installation-id": "0eb9e8bc-9725-4bd5-a382-fe92c716b3c7",
        "app-session-id": "4699341c-6f94-4481-af99-041b43d24623",
        "user-agent": "Dalvik/2.1.0",
        "content-type": "application/json"
    }
    
    data = {
        "mobile": phone_number[1:],
        "email": "eukeei@gmail.com",
        "referral_code": None,
        "geo_region_id": None
    }
    
    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=data)
        
        # Return the response text
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": sr(e)}