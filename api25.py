import requests
from bs4 import BeautifulSoup

def send_request(phone_number):
    try:
        # Step 1: Fetch the `dig_nounce` value
        main_url = "https://vaporworldbd.com/"
        response = requests.get(main_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        dig_nounce = soup.find("input", {"name": "dig_nounce"}).get("value")

        # Step 2: Send the POST request
        api_url = "https://vaporworldbd.com/wp-admin/admin-ajax.php"
        payload = {
            "action": "digits_check_mob",
            "countrycode": "+880",
            "mobileNo": phone_number,
            "csrf": dig_nounce,
            "login": "2"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://vaporworldbd.com",
            "Host": "vaporworldbd.com"
        }

        post_response = requests.post(api_url, data=payload, headers=headers)
        post_response.raise_for_status()

        return post_response.text  # Return the response text

    except Exception as e:
        return f"Error: {e}"