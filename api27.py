import requests
from bs4 import BeautifulSoup

def send_request(phone_number):
    try:
        # Step 1: Fetch the CSRF token and 'doOver' cookie
        main_url = "https://www.12bang.com/register"
        response = requests.get(main_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("meta", {"name": "csrf-token"})["content"] if soup.find("meta", {"name": "csrf-token"}) else None

        cookies = response.headers.get("set-cookie")
        doOver = None
        if cookies and "doOver=" in cookies:
            doOver = cookies.split("doOver=")[1].split(";")[0]

        if not csrf_token or not doOver:
            return "Error: Failed to retrieve CSRF token or 'doOver' cookie."

        # Step 2: Send the POST request to get OTP
        api_url = "https://www.12bang.com/getOTP"
        payload = {
            "mobileno": phone_number[1:],  # Remove the leading '+' from the phone number
            "contact_country": "880"
        }
        headers = {
            "Host": "www.12bang.com",
            "x-csrf-token": csrf_token,
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.12bang.com",
            "Referer": "https://www.12bang.com/register",
            "Cookie": f"doOver={doOver}"
        }

        post_response = requests.post(api_url, data=payload, headers=headers)
        post_response.raise_for_status()

        return post_response.json()  # Return the response JSON
    except Exception as e:
        return f"Error: {e}"