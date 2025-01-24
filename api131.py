import requests
from bs4 import BeautifulSoup

def send_request(phone_number):
    # Initial GET request to fetch the login page
    login_url = "https://salextra.com.bd/login"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Send GET request to fetch the page
    response = requests.get(login_url, headers=headers)

    # Parse the response with BeautifulSoup to find the verification token
    soup = BeautifulSoup(response.text, "html.parser")
    token_input = soup.find("input", {"name": "__RequestVerificationToken"})
    
    if token_input:
        token_value = token_input.get("value")
    else:
        raise Exception("__RequestVerificationToken not found on the page.")
    
    # Extracting .Nop.Antiforgery token from cookies
    set_cookie = response.headers.get("Set-Cookie")
    antiforgery_token = None
    
    if set_cookie:
        for cookie in set_cookie.split(";"):
            if ".Nop.Antiforgery=" in cookie:
                antiforgery_token = cookie.split("=")[1]
                break
    
    if not antiforgery_token:
        raise Exception(".Nop.Antiforgery token not found in the cookies.")
    
    # Post URL for checking username availability
    post_url = "https://salextra.com.bd/customer/checkusernameavailabilityonregistration"
    post_headers = {
        "Host": "salextra.com.bd",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://salextra.com.bd",
        "Cookie": f".Nop.Antiforgery={antiforgery_token}",
    }

    # Data to be sent in the POST request
    post_data = {
        "username": phone_number,
        "loginType": "MOBILE",
        "__RequestVerificationToken": token_value,
    }

    try:
        # Sending the POST request
        post_response = requests.post(post_url, headers=post_headers, data=post_data)
        post_response.raise_for_status()  # Raise an error for bad status codes
        return post_response.text  # Return the response text
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"