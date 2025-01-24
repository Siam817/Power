import requests

def send_request(phone_number):
    url = "https://www.nrbbazaar.com/Customer/RequestOtpForRegistration"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": ".Nop.Antiforgery=CfDJ8N5UM1Mg0_JFs4qu7TCIBSzGu689vm8mbvSPQ743hQSg8CQN0NF_XzfjEsi78OgkEPagdV_jE0-Bv17i3ToM1axTnWqbYcicXyGSwLVIJt-Jpak2l8yoNfuDZsgWG4Hlg4xPW4OOpCtcsf5xmMkdvFk"
    }
    data = {
        "phoneNumber": phone_number,
        "email": "example@gmail.com",
        "__RequestVerificationToken": "CfDJ8OTdK55f1KtKpMVto1XODz36P2tWXfyeot9aYuxWqkd81qABD_JFUva73ce2L5ftYmqCgwInZKUHisKU3mWb6DkYgBFDg4QIej8YwHP3BQ3fQvgBfc6mbMjVua7p-AT4MEPtgYhLexJmTxl7enCosqA"
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": sr(e)}