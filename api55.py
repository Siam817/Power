import requests

def send_request(phone_number):

    url = "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    data = f'{"device_uuid":"c65m117af809e65fe70dc986","firebase_token":"ei4LX14HQzmGfRXP_Nz5et:APA91bGs4IBgyO6qNJqCEKnY4ctWNTI7m10Emt0FLf4M5Mv2RwvbuJdT_O8OC37zIVXa2jb9Zhi8FldVfOs_ev3dL8PLWMboYDaMK_6gETBqQ1KloDL0W1aew9QCG8362WFckHa7txKm","geo_location":{"lat":0.0,"long":0.0},"mno":"Airtel","wallet_number":"{phone_number}","referral":""}'

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()  # Parse and return JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}