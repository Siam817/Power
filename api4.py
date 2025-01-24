import requests

def send_request(phone_number):
    url = f"https://online.utkorsho.tech/Registration?__RequestVerificationToken=Gn9BH_5Nl4FuQxigUHr4Mp8Ss_KKv_TbT5CBZSzm5MoSJ9GZqi_RdeBIcR_Mwe80-HkGDP3d3PBHacFXb6QBUlyyKeIo90cbM7XHsbN-0M41&ReturnUrl=&nickName=Rahat&mobileNumber=88{phone_number}"
    try:
        response = requests.get(url)
        return response  # Return the full response text
    except Exception as e:
        return str(e)  # Return error message if an exception occurs