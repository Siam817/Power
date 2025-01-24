import requests
import re

def send_request(phone_number):
    """
    Send a request to check account existence using phone number.
    """
    try:
        # Step 1: Fetch CSRF token and session ID
        url = "https://www.ictexpertbd.com/student/login"
        headers = {
            "Host": "www.ictexpertbd.com",
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Extract CSRF token
        csrf_token_match = re.search(r'<meta name="csrf-token" content="(.*?)">', response.text)
        csrf_token = csrf_token_match.group(1) if csrf_token_match else None

        # Extract session ID
        cookies = response.headers.get('Set-Cookie', '')
        session_id_match = re.search(r'ict_expert_session=(.*?);', cookies)
        session_id = session_id_match.group(1) if session_id_match else None

        if not csrf_token or not session_id:
            return "Error: Failed to fetch CSRF token or session ID."

        # Step 2: Send POST request
        post_url = "https://www.ictexpertbd.com/student/exist-account"
        headers.update({
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.ictexpertbd.com/student/login",
            "X-CSRF-Token": csrf_token,
            "Cookie": f"ict_expert_session={session_id}"
        })
        data = {
            "phone": phone_number
        }

        post_response = requests.post(post_url, headers=headers, data=data)
        post_response.raise_for_status()

        return post_response.json()  # Return the response JSON
    except Exception as e:
        return f"Error: {e}"