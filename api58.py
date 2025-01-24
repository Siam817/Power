import requests
import json

def send_request(phone_number):
    url = "https://api-gateway.sundarbancourierltd.com/graphql"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "",
        "Origin": "https://customer.sundarbancourierltd.com"
    }

    # Define the GraphQL query and variables
    data = {
        "operationName": "CreateAccessToken",
        "variables": {
            "accessTokenFilter": {
                "userName": phone_number
            }
        },
        "query": """
            mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {
                createAccessToken(accessTokenFilter: $accessTokenFilter) {
                    message
                    statusCode
                    result {
                        phone
                        otpCounter
                        __typename
                    }
                    __typename
                }
            }
        """
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check if request was successful
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}