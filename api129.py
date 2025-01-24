import requests

def send_request(phone_number):
    # Endpoint URL
    url = "https://www.thebodyshop.com.bd/smspro/customer/register/"
    
    # Headers
    headers = {
        "Host": "www.thebodyshop.com.bd",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.thebodyshop.com.bd"
    }
    
    # Data
    data = {
        "mobile": f"880{phone_number}"
    }
    
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"