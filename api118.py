import requests

def send_request(phone_number):
    # Endpoint URL
    url = f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/wap/88{phone_number}"

    # Headers
    headers = {
        "Host": "api.mygp.cinematic.mobi",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://cinematic.mobi"
    }

    # JSON Payload
    data = {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Authorization": "Bearer 1pake4mh5ln64h5t26kpvm3iri"
        }
    }

    try:
        # Sending POST request
        response = requests.post(url, headers=headers, json=data)
        return response.text
    except Exception as e:
        return str(e)