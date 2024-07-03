# import required modules
import requests
import json

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"

def success_get_access_token() -> str:

    payload_register = {
        "name": "Toko Example",
        "email": "hello_toko@gmail.com",
        "password": "12345678toko",
    }

    # Making a post request (register)
    response_register = requests.post(BASE_URL + "/registration", data=payload_register)

    # Convert json into dictionary
    response_json_register = response_register.json()

    # Parse the response body
    email_regist_resp = response_json_register.get('data').get('email')
    password_regist_req = payload_register.get('password')

    payload_login = {
        "email": email_regist_resp,
        "password": password_regist_req,
    }

    # Making a post request (login)
    response_login = requests.post(BASE_URL + "/authentications", data=payload_login)

    # Convert json into dictionary
    response_json_login = response_login.json()

    # Parse the response body
    access_token = response_json_login.get('data').get('accessToken')

    return access_token
