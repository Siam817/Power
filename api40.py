import requests

def send_request(phone_number):
    url = "https://api.waltonplaza.com.bd/graphql"
    payload = {
        "operationName": "createCustomerOtp",
        "variables": {
            "auth": {
                "countryCode": "880",
                "deviceUuid": "4c735750-6bc9-11ee-84c0-190466a47baa",
                "phone": phone_number  # Dynamically set phone number
            }
        },
        "query": """
        mutation createCustomerOtp($auth: CustomerAuthInput!, $device: DeviceInput) {
            createCustomerOtp(auth: $auth, device: $device) {
                message
                result {
                    id
                    __typename
                }
                statusCode
                __typename
            }
        }
        """
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Send POST request
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}