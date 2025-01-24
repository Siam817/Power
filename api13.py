import requests

def send_request(phone_number):
    url = "https://pbs.com.bd/login/?handler=UserGetOtp"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "XSRF-Token": "CfDJ8C8FhGbSUB1CplCwhmaw48FrjIGNq5sPRk0G6VzBicZtPJrEXDCoqGMiBTb3Fetxypt-480avEXqJS_WJVdEWQeDCz0mKIQO4odODIqIopHM8qh50R7CF3bOGHOtF22Pt-pgeyMhHQTk2t2inqJMRyw",
        "Cookie": (
            ".AspNetCore.Antiforgery.B6RPubf2LMI=CfDJ8C8FhGbSUB1CplCwhmaw48HSKnE-hppep13XT5NAyk3laCHJb_oP0B1wPBZQP-hzP8Z2CAclzIeEqkFAMeWJS8xWzyiIMY_sMlsO7WzVcxmONd9WUDnzazvUlK9zFOY8h6Pwx1xsDD9fgtr2ltr9qHE;"
        )
    }
    payload = {
        "UserName": "",
        "UserPassword": "",
        "chkRememberPassword": "",
        "MobileNo": phone_number,  # Use dynamic phone number
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        return response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"