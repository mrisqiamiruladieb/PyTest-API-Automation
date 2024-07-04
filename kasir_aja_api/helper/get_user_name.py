# import required modules
import requests
import json
from jsonschema import validate
import random

# path for test.py
# from get_access_token import success_get_access_token

# path for testing
from .get_access_token import success_get_access_token

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"

# create a user request
def success_get_user_name() -> str:

    # Generate random number
    rand_int = random.randint(1, 999)

    payload_create_user = {
        "name": "kasir-" + str(rand_int),
        "email": "user-" + str(rand_int) + "@example.com",
        "password": "jiasda2321@"
    }

    access_token = success_get_access_token()

    headers = { "Authorization": f"Bearer {access_token}" }

    # Making a post request
    response = requests.post(BASE_URL + "/users", data=payload_create_user, headers=headers)

    # Convert json into dictionary
    response_json = response.json()

    # Parse the response body
    user_name = response_json.get('data').get('name')

    return user_name